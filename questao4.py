'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor 
total mensal da distribuidora.'''
import os 
os.system('cls')

sp=67836.43
rj=36678.66
mg=29229.88
es=27165.48
ou=19849.53


total=(sp+rj+mg+es+ou)
print(f"O pecentual de representação do estado de São Paulo no valor mensal é de{(sp/total)*100}%.\nO pecentual de representação do estado do Rio de janeiro no valor mensal é de{(rj/total)*100}%.\nO pecentual de representação do estado de Minas Gerais no valor mensal é de{(mg/total)*100}%.\nO pecentual de representação do estado do Espirito Santo no valor mensal é de{(es/total)*100}%.\nO percentual de respresentação de outros estados no valor mensal da empresa é de {(ou/total)*100}%.")