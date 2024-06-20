<h1><b>Jogo-da-forca-v1</b></h1> 

## Objetivo
O presente projeto tem por objetivo apresentar o desenvolvimento de um jogo da forca simples programado com a linguagem Python capaz de selecionar aleatoriamente uma palavra de um objeto do tipo dicionário (chave e valor) da linguagem Python. Não estava no planejamento do trabalho realizar um trabalho pensando na simplificação e otimização do tempo de execução do código, mas sim o aprimoramento e desenvolvimento de conceitos e fundamentos vistos na prática. Entre os fundamentos abordados, está a utilização do pacote <code>random</code>, tratamento de arquivos csv e transformação dos dados em dicionário. Além da utilização de planilha e do ChatGPT para a geração das palavras a serem adivinhadas pelo usuário.

## Ferramentas
* Python 3.10.13
* ChatGPT-4
* Google Sheets

## Desenvolvimento
Inicialmente o ChatGPT foi utilizado para gerar 50 palavras de cada um dos grupos de palavras pré-definidos, dos quais foram escolhidos países, filmes famosos, frutas, nomes comuns e séries famosas, como os grupos. O chatGPT então gerou as informações abaixo.

![image](https://github.com/mathwatanabe/Jogo-da-forca-v1/assets/170628618/e30beea1-e22d-48b5-8ff5-6c34b9b3bc9a)

Essas informações foram copiadas para uma planilha no Google Sheets para que fossem organizadas da melhor forma para ser tratado em um arquivo csv. Nessa planilha, cada palavra foi separada em uma célula de uma coluna específica e, posteriormente, as linhas foram transpostas para se ter uma melhor organização a ser tratada no csv. Todos esses procedimentos são apresentados no arquivo do Jupyter Notebook.

![image](https://github.com/mathwatanabe/Jogo-da-forca-v1/assets/170628618/c9b4778b-c7f6-4d6c-8229-641ad6bd0a0f)

Com o arquivo em csv, ele foi aberto para ser tratado e transformado em um dicionário com uma chave associada a cada palavra e um valor associado a um grupo de palavras. O bloco de código abaixo realiza esse processo
```neon
#Abrindo e guardando a leitura do arquivo csv na variável 'arquivo'
arquivo = open('Palavras-ChatGPT.csv').read()
#Como cada linha estava sendo definida pelo caracter '\n', foi utilizado o método split para quebrar cada linha em uma lista
rows = arquivo.split('\n')
#List Comprehension para separar cada uma das palavras em um elemento específico de uma lista de listas
rows_celulas = [row.split(',') for row in rows]
#Colocando cada palavra em uma lista de listas de palavras
palavras = [rows_celulas[i] for i in range(1,len(rows_celulas))]
#Colocando cada classe em uma lista específica
classes = rows_celulas[0]
dicionário_palavras = {}
for i in range(0,len(classes)):
    for row in palavras:
        dicionário_palavras[row[i]] = classes[i]
```

Esse código pode ser acessado diretamente no arquivo '<a href=https://github.com/mathwatanabe/Jogo-da-forca-v1/blob/main/tratamento-csv.ipynb>tratamento-csv.ipynb</a>'.

Todo esse procedimento poderia ser realizado de forma mais simples e rápida pela utilização da biblioteca Pandas, com a utilização de Dataframes, no entanto, optou-se por esse outro caminho para o aprimoramento dos fundamentos e conceitos aprendidos na teoria.

O próximo passo foi importar a biblioteca <code>random</code> que foi utilizada para selecionar um item aleatório do dicionário e foi importado o pacote <code>os</code> para a criação de uma função responsável por limpar a tela.
```neon
import random
from os import system, name
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
```
Posteriormente foi criada uma função capaz de substituir, nas palavras que possuem acento, a letra acentuada pela letra sem a marcação gráfica. Isso foi necessário para que o usuário não necessitasse diferenciar as letras acentuadas ou não acentuadas, e para o programa não ter diferenciação entre a letra acentuada ou não. O resto do código pode ser encontrado no arquivo '<a href=https://github.com/mathwatanabe/Jogo-da-forca-v1/blob/main/Jogo-da-forca-v1.py>Jogo-da-forca-v1.py</a>'
```neon
def substituir(palavra):
    #Essa variável será a palavra escolhida do dicionário de forma aleatória posteriormente
    palavra = str(palavra)
    #A função lower() foi utilizada para não necessitar da diferenciação entre letras no início da palavra ou no meio
    palavra2 = palavra.lower()
    if 'á' in palavra2:
        palavra2 = palavra2.replace('á','a')
    if 'â' in palavra:
        palavra2 = palavra2.replace('â','a')
    if 'ã' in palavra:
        palavra2 = palavra2.replace('ã','a')
```
Uma função para a criação automática de um gabarito, no qual, as letras eram substituídas por '_'.
```neon
def letras_palavra(charada):
    memoria_resposta = []
    #A variável charada serve para serve para receber a palavra a ser adivinhada
    for letra in charada:
        #Se a palavra possuir algum dos caracteres abaixo, eles não serão substituídos por '_'
        if letra == '-' or letra == ')' or letra == '(' or letra == '.' or letra == ' ' or letra == ',':
            memoria_resposta.append(letra)
        elif letra == '1' or letra == '2' or letra == '3' or letra == '4' or letra == '5' or letra == '6' or letra == '7' or letra == '8' or letra == '9' or letra == '0':
            memoria_resposta.append(letra)
        #As letras são substituídas por '_'
        else:
            memoria_resposta.append('_')
    return memoria_resposta
```
Por fim, foi criado o bloco de código responsável pela dinâmica do jogo. Mais detalhes acerca do código podem ser encontrados em '<a href=https://github.com/mathwatanabe/Jogo-da-forca-v1/blob/main/Jogo-da-forca-v1.py>Jogo-da-forca-v1.py</a>'. Em resumo, a função <code>choice</code> foi chamada para realizar a escolha aleatória no dicionário contendo as palavras a serem adivinhadas.
```neon
def game():
    #Execução da limpeza de tela
    limpa_tela()
    dicionário_palavras = {'Brasil': 'Países', 'Estados Unidos': 'Países', 'China': 'Países', 'Índia': 'Países', 'Japão': 'Países', ..., 'Ozark': 'Séries Famosas'}
    #Guardando a palavra definida aleatoriamente pela função choice() do pacote random
    palavra1, grupo = random.choice(list(dicionário_palavras.items()))
```
Foram realizados 3 passos importantes, a criação de uma lista para guardar as letras incorretas que foram escolhidas, definição de uma variável <code>tentativas</code> para guardar a quantidade de tentativas restantes do usuário e a utilização da função <code>substituir()</code> definida anteriormente para retirar os acentos das palavras.
```neon
def game():
    ...

    #Uma lista é definida para gravar as letras erradas já escolhidas
    letras_erradas = []
    tentativas = int
    
    #Retirar os acentos da palavra escolhida para ser adivinhada
    palavra_sem_acento = substituir(palavra1)
```
Foi definida a quantidade de tentativas de acordo com o grupo de palavras.
```neon
def game():
    ...

 #Definição da quantidade máxima de tentativas para cada grupo de palavras específico
    if grupo == 'Países':
        tentativas = 5
    elif grupo == 'Filmes Famosos':
        tentativas = 8
    elif grupo == 'Frutas':
        tentativas = 5
    elif grupo == 'Nomes Comuns':
        tentativas = 7
    elif grupo == 'Séries Famosas':
        tentativas = 10

    #Definir a quantidade de '_' que irão aparecer no gabarito da palavra
    m = letras_palavra(palavra1)
```
Por último o bloco de execução principal para apresentar informações importantes para o usuário foi definido, como as seguintes informações, quantidade de tentativas, gabarito com as letras corretas já adivinhadas e letras incorretas. Além disso, esse bloco mantém um loop até que o usuário tenha ganhado ou tenha perdido por não ter mais tentativas. Para verificar se o usuário ganhou, o condicional if é utilizado para verificar a existência do caracter '_' no gabarito, se não houver, isso significa que o usuário adivinhou todas as letras palavra.
```neon
def game():
    ...

    while tentativas > 0:
        #Para verificar se todas as letras foram adivinhadas
        if '_' not in m:
            #Se não houver, então o usuário ganhou o jogo
            print(f'----------\nVocê ganhou! A resposta é {palavra1}.')
            return
        print('\n----------\n')
        #Mostrar o gabarito na tela
        print(' '.join(m))
        #Mostrar quantidade de tentativas
        print(f'Você ainda tem {tentativas} tentativas.')
        #Mostrar a letras erradas
        print('Letras erradas:',' '.join(letras_erradas))
```
Ainda no loop <code>while</code>, o pedido de inserção e verificação da letra inserida foi definido como representado abaixo. O condicional foi utilizado para, enquanto o usuário não inserisse uma letra válida no programa ou se ele inserisse uma letra incorreta já tentada, ele permaneceria pedindo a inserção da letra.
```neon
def game():
    ...

        #Pedir ao usuário a inserção de uma letra
        letra = input('Insira uma letra: ')
        #Essa condicional serve para não aceitar caracteres inválidos
        if len(letra) != 1 or letra == 'â' or letra == 'ã' or letra == 'é' or letra == 'ê' or letra == 'í' or letra == 'î' or letra == 'ó' or letra =='ô' or letra == 'ú' or letra == 'û':
            continue
        #Se a letra inserida já estiver sido tentada, mas não estiver na palavra, o loop recomeça
        elif letra.upper() in letras_erradas:
            continue
```
O bloco de código utilizado quando uma letra correta fosse inserida. Nele, a letra correta substituiria no gabarito o caracter '_' pela letra correta adivinhada.
```neon
def game():
    ...

        #Se a letra escolhida estiver na palavra, segue essa condicional
        elif letra.lower() in palavra_sem_acento.lower():
            print(f'A letra "{letra.upper()}" está na palavra!')
            #Verificar e substituir onde a letra escolhida de forma correta será colocada
            for i in range(0,len(palavra1)):
                #Comparar a letra minúscula com a palavra apenas com letras minúsculas para não ocorrer erro de comparação entre maiúscula e minúscula
                if letra.lower() == palavra_sem_acento.lower()[i]:
                    #Substituir o '_' no gabarito pela letra correta
                    m[i] = letra.upper()
                else:
                    continue
```
Por último, se fosse inserida uma letra incorreta, a parte representada abaixo seria responsável por identificar e tratar tal erro, reduzindo o número de tentivas e adicionando a letra errada na lista de letras erradas.
```neon
def game():
    ...

        #Se a letra escolhida não estiver na palavra e ainda não tiver sido verificada
        elif letra.lower() not in palavra_sem_acento.lower():
            #Reduzir o número de tentativas em 1
            tentativas -= 1
            #Adicionar a letra errada à lista de letras incorretas
            letras_erradas.append(letra.upper())
            print(f'A letra "{letra.upper()}" não está na palavra!')
            #Verificar se ainda há tentativas
            if tentativas == 0:
                #Se não houver mais tentativas, mostrar que o usuário perdeu
                print(f'----------\nVocê perdeu! A resposta era {palavra1}')
```
Com o código para execução do jogo finalizado, os blocos foram executados conforme demonstrado abaixo:
```neon
if __name__ == "__main__":
    game()
    print('Até a próxima!')
```
