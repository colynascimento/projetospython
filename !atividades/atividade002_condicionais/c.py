# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 25/04/2024
# Atividade 002: Condicionais

# C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de 
# velocidade para ajudar a promover a segurança nas estradas. Eles precisam de um 
# programa que permita aos usuários inserir a velocidade de um carro e, em seguida,
# exibir na tela uma mensagem adequada com base na velocidade fornecida. O objetivo 
# principal é alertar os motoristas caso ultrapassem o limite de velocidade de 
# 60km/h, incentivando-os a dirigir dentro dos limites legais e, assim, reduzir o 
# risco de acidentes.

import os


os.system('cls')

# Variável
velocidade = float(input('Insira a velocidade do carro em km/h: '))

# Condicional e Saída
if velocidade > 60:
    print('Atenção! A velocidade atual está acima do limite permitido'
          'de 60km/h, por favor, reduza para sua segurança.')
else:
    print('A velocidade do carro está adequada, mantenha o cuidado :)')