# CARLOS GAMES - Sistema de Controle de Estoque

Projeto feito em Python durante a graduação em Engenharia de Software.

## Sobre o projeto

Antes de estudar programação, trabalhei um tempo numa loja de peças de games e PC. Quando precisei escolher um tema para esse projeto, decidi usar essa experiência: criar um sistema de controle de estoque para uma loja de games.

A ideia era simples na teoria e mais trabalhosa na prática: acompanhar o estoque de produtos, registrar quando chegam novas unidades e quando saem por venda, sem deixar os dados baguncem com o tempo. Sem framework, sem biblioteca externa - só lógica, Python puro e bastante tentativa e erro.

## O que o sistema faz

- Exibe o estoque atual, com quantidade e preço de cada produto
- Registra entrada de produtos (chegada de novas unidades)
- Registra saída de produtos (venda), verificando se há quantidade suficiente antes de subtrair
- Avisa quando o produto não é encontrado ou quando o estoque é insuficiente para a saída

## Tecnologias

Python. O estoque é armazenado como um dicionário de dicionários - escolhi essa estrutura porque o nome do produto funciona como chave única, permitindo acessar direto os dados de cada item (ex: `estoque["PlayStation 5 slim"]`) sem precisar percorrer uma lista inteira.

## Resultado

Fechei o projeto com nota 0.9/1.0. O feedback do professor foi principalmente sobre a organização da lógica.

## O que eu levo desse projeto

Foi o primeiro projeto que me fez sentir que eu conseguia, de fato, transformar um problema real (mesmo que fictício) em código que funciona do início ao fim. Também foi onde percebi que minha experiência anterior - lidando com produtos, estoque, processos - não fica "para trás" quando você muda de área. Ela vira ponto de partida.

## Como rodar

python Carlos-Games-Stock.py

## Autor

Carlos - [[LinkedIn](#)](https://www.linkedin.com/in/carlos-cabral-3b45522b7/).
