from sympy.combinatorics import Permutation
from typing import Dict, List, Tuple


class pessoa:
    def __init__(self, corpo, mente):
        self.corpo = corpo
        self.mente = mente

    def __repr__(self):
        return f"(corpo de {self.corpo}, mente de {self.mente})"
    
    def estado_natural(self):
        return self.corpo == self.mente  # Simplificação do retorno


class teorema_de_futurama:
    def __init__(self, pessoas: Dict[str, pessoa]):
        self.pessoas = pessoas | {'x': pessoa('x', 'x'), 'y': pessoa('y', 'y')}

    def aplicar_transposicao(self, a: str, b: str) -> None:
        self.pessoas[a].mente, self.pessoas[b].mente = self.pessoas[b].mente, self.pessoas[a].mente

    def permutacao(self) -> Permutation:
        pessoas_alvo = {k: v for k, v in self.pessoas.items() if k not in ['x', 'y']}
        indices = {name: i for i, name in enumerate(sorted(pessoas_alvo))}
        return Permutation([indices[p.mente] for p in pessoas_alvo.values() if p.mente in indices])
    
    def solucionar_ciclo(self, cycle: List[str]) -> List[Tuple[str, str]]:
        if len(cycle) <= 1:
            return []
        
        i = len(cycle) // 2
        return ([('x', trocas) for trocas in cycle[:i]] + 
                [('y', trocas) for trocas in cycle[i:]] +
                ([('x', cycle[i])] if i < len(cycle) else []) +
                [('y', cycle[0])])
    
    def resolver(self) -> List[Tuple[str, str]]:
        ciclos = self.permutacao().cyclic_form
        mapeiar_nome = {i: name for i, name in enumerate(sorted(n for n in self.pessoas if n not in ['x', 'y']))}

        solucao = []
        n_de_ciclos = 0

        for ciclo in ciclos:
            if len(ciclo) <= 1:
                continue

            ciclo_de_nome = [mapeiar_nome[i] for i in ciclo]
            solucao.extend(self.solucionar_ciclo(ciclo_de_nome))
            n_de_ciclos += 1 

        if n_de_ciclos % 2:
            solucao.append(('x', 'y'))
        return solucao   

    def aplicar_solucao(self) -> List[Tuple[str, str]]:
        solution = self.resolver()  # Corrigido o nome do método
        
        print("Aplicando sequência de transposições:\n")
        for idx, (a, b) in enumerate(solution, 1):
            before_a = (self.pessoas[a].corpo, self.pessoas[a].mente)
            before_b = (self.pessoas[b].corpo, self.pessoas[b].mente)
            
            self.aplicar_transposicao(a, b)  # Corrigido o nome do método
            
            after_a = (self.pessoas[a].corpo, self.pessoas[a].mente)
            after_b = (self.pessoas[b].corpo, self.pessoas[b].mente)
            
            print(f"{idx}ª troca:")
            print(f"Corpo {before_a[0]}, Mente {before_a[1]} -> "
                  f"Corpo {after_a[0]}, Mente {after_a[1]}")
            print(f"Corpo {before_b[0]}, Mente {before_b[1]} -> "
                  f"Corpo {after_b[0]}, Mente {after_b[1]}\n")
        
        main_people = (p for n, p in self.pessoas.items() if n not in ['x', 'y'])
        if all(p.estado_natural() for p in main_people):  # Corrigido o nome do método
            print("\nTodos retornaram ao estado natural!")
        else:
            print("\nERRO: Nem todos retornaram ao estado natural!")
            
        return solution     
    
# Aplicação do teorema 

if __name__ == "__main__":
    pessoas = {
        'Amy': pessoa('Amy', 'Amy'),
        'Bender': pessoa('Bender', 'Bender'),
        'Professor': pessoa('Professor', 'Professor')
    }

    teorema = teorema_de_futurama(pessoas)

    print("Aplicando transposições iniciais:")
    for a, b in [('Amy', 'Bender'), ('Bender', 'Professor')]:
        print(f"<{a},{b}>")
        teorema.aplicar_transposicao(a, b)

    print("\nEstado após transposições iniciais:")
    for name, p in pessoas.items():
        print(p)
    
    # Chamar corretamente a função
    solution = teorema.aplicar_solucao()   

    print("\nEstado final:")
    for name, p in pessoas.items():
        print(f"{p} - Natural: {p.estado_natural()}")