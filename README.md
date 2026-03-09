![teorema futurama quadro](https://github.com/user-attachments/assets/cad51bac-6784-4f9a-97f4-5fa501cbe347)

🛸 Futurama: Aplicação do algoritmo da troca de mentes em Python usando Sympy

Este projeto é uma implementação em Python do famoso Teorema de Futurama, criado pelo roteirista (e PhD em matemática) Ken Keeler para o episódio "O Prisioneiro de Benda".

🧠 O Problema
No episódio, o Professor e Amy inventam uma máquina de troca de mentes. No entanto, a máquina possui uma falha fatal: duas pessoas não podem usar a máquina juntas mais de uma vez, sendo sempre necessário uma pessoa extra (que nunca usou a máquina)  para começar outra troca de mentes. 

Após várias trocas confusas entre a tripulação do Planet Express, todos acabam em corpos errados. O desafio matemático é: Qual é o mínimo de pessoas necessário para trazer todos de volta aos seus corpos originais ?


🧠 Como funciona a solução? 

O problema da troca de corpos pode ser modelado usando Teoria dos Grupos, especificamente o estudo de permutações. 

Primeiro, o algoritmo analisa o estado atual de todas as pessoas e cria uma permutação usando a biblioteca sympy. Ele agrupa as mentes trocadas em ciclos disjuntos.
Por exemplo, se a mente de Amy está no Professor, a do Professor no Bender, e a do Bender na Amy, temos um ciclo fechado:
(Amy→Professor→Bender)

Os "Coringas" (X e Y)

Para burlar as regras e resolver os ciclos, o algoritmo prova que precisamos adicionar exatamente dois novos corpos que nunca usaram a máquina com ninguém. No código, eles são instanciados como x e y.

Resolvendo Ciclos Individualmente
Para cada ciclo de mentes bagunçadas, a função solucionar_ciclo divide o problema ao meio (variável i = len(cycle) // 2):

O coringa x troca de corpo com a primeira metade do ciclo.

O coringa y troca de corpo com a segunda metade.

Depois, x e y fazem trocas estratégicas com as "pontas" dessa divisão (cycle[i] e cycle[0]).
Isso permite que cada mente seja depositada em seu corpo original sem nunca repetir uma dupla na máquina.

Sempre que resolvemos um ciclo usando o método acima, as mentes dos coringas x e y acabam trocadas entre si.

Se houver um número par de ciclos, as mentes de x e y voltarão aos seus próprios corpos naturalmente ao final do processo.
Se houver um número ímpar de ciclos (variável n_de_ciclos % 2), o algoritmo adiciona uma última troca: ('x', 'y'), garantindo que     os coringas também voltem ao estado natural.

<img width="465" height="693" alt="saida teorema de futurama" src="https://github.com/user-attachments/assets/df0a3d64-f8fe-4e00-8b3d-521f622a4160" />

