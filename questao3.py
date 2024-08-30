'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
import json
import os 
os.system('cls')


with open(".\processo seletivo - Target sistemas\dados.json", encoding='utf-8') as data:
    dados=json.load(data)
maior_faturamento=float('-inf')
menor_faturamento=float('inf')
soma=0
dias_trabalhados=0
acima_media=0

for i in dados:
    if i['valor']>0:
        dias_trabalhados+=1
    if i['valor']<menor_faturamento:
        menor_faturamento=i['valor']
    if i['valor']>maior_faturamento:
        maior_faturamento=i['valor']
    soma+=i['valor']
media_vendas=soma/dias_trabalhados

for i in dados:
    if i['valor']>media_vendas:
        dias_trabalhados+=1
print(f'A menor receita diaria da empresa foi de R$ {menor_faturamento}.\n A maior receita diaria da empreasa foi de R$ {maior_faturamento}.\nOs dias com receita maior que a media da empresa foram:{media_vendas}.')

