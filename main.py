### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# qualidade = 20
# preco = 10

# if isinstance(qualidade,int) and isinstance(preco,int):
#     if qualidade > 0 and preco > 0:
#         print ('tudo certo')
#     else: 
#         print ('dados invalidos')
# else: 
#     print('o dado não é um número')


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# temperatura = int(input())

# if temperatura >= 20 :
#     print('Alta')
# elif temperatura < 20 and temperatura >= 0 :
#     print('Media')
# else :
#     print('Baixa')



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = [{'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
# {'timestamp': '2021-06-23 10:10:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
# {'timestamp': '2021-06-23 10:20:00', 'level': 'OK', 'message': 'Falha na conexão'},
# {'timestamp': '2021-06-23 10:30:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
# {'timestamp': '2021-06-23 10:40:00', 'level': 'ERROR', 'message': 'Falha na conexão'}]

# contagem_erros = {}
# for entry in log:
#     if entry['level'] == 'ERROR': 
#         contagem_erros[entry['timestamp']] = contagem_erros.get(entry['timestamp'],0) +1
# print (contagem_erros)

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# idade = int(input('Digite sua idade :'))
# email = str(input('Digite seu email :'))

# if email.find("@"):
#     print ('Seu email é válido')
# else : 
#     print ('Dados inválidos')


# if isinstance(idade,int) :
#     if idade in range(18,66):
#         print ('Sua idade é válida')
#     else :
#         print ('Dados inválidos')


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# # Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao = [{'valor': 12000, 'hora': 20},
#             {'valor': 800, 'hora': 12},
#             {'valor': 1000, 'hora': 22},
#             {'valor': 200, 'hora': 18},
#             {'valor': 12000, 'hora': 10},
#             {'valor': 1000, 'hora': 11},
#             {'valor': 100, 'hora': 21},
#             {'valor': 12000, 'hora': 8}]

# transacao_suspeita = []

# for suspeitos in transacao:
#     if suspeitos['valor'] >= 10000 or suspeitos['hora'] < 9 or suspeitos['hora'] > 18:
#         transacao_suspeita.append(suspeitos)
#     else:
#         pass
# print (transacao_suspeita)

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.


# texto = str("Lorem Morbi dolor sit Morbi, consectetur adipiscing elit. In faucibus non libero ac tempus. In eu Morbi ipsum. Sed elementum dignissim felis vitae maximus. Morbi non urna nec neque sodales hendrerit. Sed iaculis tincidunt massa sed aliquam. Morbi nec justo nunc. Morbi pellentesque erat risus, a laoreet ex mollis vitae.Pellentesque auctor ante nisi, id condimentum risus maximus sed. Nullam elementum, diam non posuere auctor, magna enim vulputate nulla, sit amet iaculis quam dolor nec risus. Aenean sit amet neque ipsum. Quisque sed lectus ullamcorper, pulvinar nulla at, condimentum orci. Proin quam nibh, sodales sit amet magna porta, ultricies placerat eros. Praesent ultricies ullamcorper faucibus. Morbi sagittis a sem lobortis commodo. Donec tellus dui, tempor sed venenatis sed, cursus eget ante.")
# result = {}
# import string
# def limpar_texto(text):
#     text_replace = text.translate(str.maketrans('','',string.punctuation))
#     print(text_replace)
#     text_lower = text_replace.lower()
#     text_split = text_lower.split()
#     return text_split

# palavras = limpar_texto(texto)


# for palavra in palavras:
#     if palavra in result:
#         result[palavra] += +1
#     else:
#         result[palavra] = 1
# print(result)
        



### Exercício 7. Normalização de Dados
# # Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# lista = [1,5,6,8,9,12,15,16]
# min_lista = min(lista)
# max_lista = max(lista)
# norm = []

# for i in lista:
#     new_value = (i - min_lista)/(max_lista - min_lista)
#     norm.append(new_value)
# print(norm)




### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando






### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# lista = [1,5,6,8,9,12,15,16]
# pares = []

# for i in lista:
#     if i%2 == 0:
#         pares.append(i)
# print(pares)



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas =  [{'categoria':"Carro",'valor':210},
#     {'categoria':"Casa",'valor':250},
#     {'categoria':"Carro",'valor':255},
#     {'categoria':"Casa",'valor':222},
#     {'categoria':"Carro",'valor':1200},
#     {'categoria':"Carro",'valor':203},
#     {'categoria':"Carro",'valor':205},
#     {'categoria':"Casa",'valor':226},
#     {'categoria':"Casa",'valor':212},
#     {'categoria':"Carro",'valor':200}]

# result = {'Casa': int(),'Carro': int()}
# for venda in vendas:
#     if venda["categoria"] == "Casa":
#         result["Casa"] += +venda["valor"]
#     else: 
#         result["Carro"] += +venda["valor"]
# print (result)
    

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# texto = ""
# dados = []
# while texto.lower() != "sair":
#     texto = input("Digite uma palavra ou sair para finalizar :")
#     if texto.lower()!= "sair":
#         dados.append(texto)
#     else:
#         break

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# import random
# ''
# certo = int()
# tentativa = int(input("Digite um numero de 1 a 15 :  "))
# result = int()

# while certo != tentativa:
#     certo = random.randint(1,15)
#     print(certo)
#     result += +1
# if certo == tentativa:
#     print(f'Parabéns, você acertou na {result} tentativa')


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# paginas_api = 8
# pagina_atual = 1

# while pagina_atual < paginas_api:
#     print(f'Processando {pagina_atual} de {paginas_api} paginas disponíveis')
#     pagina_atual += +1
# print(f'Processo finalizado. {pagina_atual} páginas foram processadas')



### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# max_tentaivas = 5
# tentativa = 1
# conexao = False

# while tentativa <= max_tentaivas:
#     print(f'Tentaiva {tentativa} de {max_tentaivas}')
#     if conexao == True:
#         print("Conexão bem sucedida")
#         break
#     tentativa += +1
# else:
#     print("Falha ao conectar, Limite de tentativas excedido")


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

texto = "Ler todo o texto até encontrar sair uma condição de para como a palavra sair ou algo do tipo"
texto = texto.split()
stop_cond  = "sair"
dados = []
for text in texto:
    while text.lower() != "sair":
        dados.append(text)
        break
    if text.lower() == "sair":
        break
print(dados)