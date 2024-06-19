import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def substituir(palavra):
    palavra = str(palavra)
    palavra2 = palavra.lower()
    if 'á' in palavra2:
        palavra2 = palavra2.replace('á','a')
    if 'â' in palavra:
        palavra2 = palavra2.replace('â','a')
    if 'ã' in palavra:
        palavra2 = palavra2.replace('ã','a')
    if 'é' in palavra:
        palavra2 = palavra2.replace('é','e')
    if 'ê' in palavra:
        palavra2 = palavra2.replace('ê','e')
    if 'í' in palavra:
        palavra2 = palavra2.replace('í','i')
    if 'î' in palavra:
        palavra2 = palavra2.replace('î','i')
    if 'ó' in palavra:
        palavra2 = palavra2.replace('ó','o')
    if 'ô' in palavra:
        palavra2 = palavra2.replace('ô','o')
    if 'õ' in palavra:
        palavra2 = palavra2.replace('õ','o')
    if 'ú' in palavra:
        palavra2 = palavra2.replace('ú','u')
    if 'û' in palavra:
        palavra2 = palavra2.replace('û','u')
    palavra2 = palavra2.capitalize()
    return palavra2

def letras_palavra(charada):
    memoria_resposta = []
    for letra in charada:
        if letra == '-' or letra == ')' or letra == '(' or letra == '.' or letra == ' ' or letra == ',':
            memoria_resposta.append(letra)
        elif letra == '1' or letra == '2' or letra == '3' or letra == '4' or letra == '5' or letra == '6' or letra == '7' or letra == '8' or letra == '9' or letra == '0':
            memoria_resposta.append(letra)
        else:
            memoria_resposta.append('_')
    return memoria_resposta

def game():
    limpa_tela()
    dicionário_palavras = {'Brasil': 'Países', 'Estados Unidos': 'Países', 'China': 'Países', 'Índia': 'Países', 'Japão': 'Países', 'Alemanha': 'Países', 'França': 'Países', 'Reino Unido': 'Países', 'Itália': 'Países', 'Canadá': 'Países', 'Rússia': 'Países', 'Austrália': 'Países', 'México': 'Países', 'Indonésia': 'Países', 'Espanha': 'Países', 'Turquia': 'Países', 'Arábia Saudita': 'Países', 'Coreia do Sul': 'Países', 'África do Sul': 'Países', 'Argentina': 'Países', 'Colômbia': 'Países', 'Egito': 'Países', 'Chile': 'Países', 'Peru': 'Países', 'Malásia': 'Países', 'Nigéria': 'Países', 'Ucrânia': 'Países', 'Polônia': 'Países', 'Holanda': 'Países', 'Bélgica': 'Países', 'Tailândia': 'Países', 'Suíça': 'Países', 'Suécia': 'Países', 'Noruega': 'Países', 'Dinamarca': 'Países', 'Finlândia': 'Países', 'Áustria': 'Países', 'Grécia': 'Países', 'Israel': 'Países', 'Hungria': 'Países', 'Portugal': 'Países', 'Irlanda': 'Países', 'Nova Zelândia': 'Países', 'Vietnã': 'Países', 'Filipinas': 'Países', 'Paquistão': 'Países', 'Irã': 'Países', 'Bangladesh': 'Países', 'Marrocos': 'Países', 'O Poderoso Chefão': 'Filmes Famosos', 'Forrest Gump': 'Filmes Famosos', 'O Senhor dos Anéis': 'Filmes Famosos', 'Star Wars': 'Filmes Famosos', 'Titanic': 'Filmes Famosos', 'Matrix': 'Filmes Famosos', 'Vingadores: Ultimato': 'Filmes Famosos', 'Jurassic Park': 'Filmes Famosos', 'Pulp Fiction': 'Filmes Famosos', 'Clube da Luta': 'Filmes Famosos', 'O Cavaleiro das Trevas': 'Filmes Famosos', 'De Volta para o Futuro': 'Filmes Famosos', 'Gladiador': 'Filmes Famosos', 'Toy Story': 'Filmes Famosos', 'E.T. - O Extraterrestre': 'Filmes Famosos', 'O Resgate do Soldado Ryan': 'Filmes Famosos', 'O Exorcista': 'Filmes Famosos', 'Indiana Jones': 'Filmes Famosos', 'Psicose': 'Filmes Famosos', 'Alien': 'Filmes Famosos', 'O Iluminado': 'Filmes Famosos', 'Coração Valente': 'Filmes Famosos', 'O Silêncio dos Inocentes': 'Filmes Famosos', 'Casablanca': 'Filmes Famosos', 'Os Caça-Fantasmas': 'Filmes Famosos', 'Tubarão': 'Filmes Famosos', 'O Grande Lebowski': 'Filmes Famosos', 'O Senhor dos Anéis: As Duas Torres': 'Filmes Famosos', 'A Origem': 'Filmes Famosos', 'Batman: O Cavaleiro das Trevas Ressurge': 'Filmes Famosos', 'O Rei Leão': 'Filmes Famosos', 'O Estranho Sem Nome': 'Filmes Famosos', 'Se7en': 'Filmes Famosos', 'Blade Runner': 'Filmes Famosos', 'Os Intocáveis': 'Filmes Famosos', 'Mad Max: Estrada da Fúria': 'Filmes Famosos', 'Harry Potter e a Pedra Filosofal': 'Filmes Famosos', 'Esqueceram de Mim': 'Filmes Famosos', 'A Vida é Bela': 'Filmes Famosos', 'Jurassic World': 'Filmes Famosos', 'Procurando Nemo': 'Filmes Famosos', 'Os Vingadores': 'Filmes Famosos', 'O Hobbit': 'Filmes Famosos', 'A Bela e a Fera': 'Filmes Famosos', 'Deadpool': 'Filmes Famosos', 'Star Trek': 'Filmes Famosos', 'Velozes e Furiosos': 'Filmes Famosos', 'Banana': 'Frutas', 'Maçã': 'Frutas', 'Abacaxi': 'Frutas', 'Laranja': 'Frutas', 'Uva': 'Frutas', 'Manga': 'Frutas', 'Morango': 'Frutas', 'Melancia': 'Frutas', 'Limão': 'Frutas', 'Pera': 'Frutas', 'Ameixa': 'Frutas', 'Kiwi': 'Frutas', 'Caju': 'Frutas', 'Goiaba': 'Frutas', 'Acerola': 'Frutas', 'Pêssego': 'Frutas', 'Melão': 'Frutas', 'Figo': 'Frutas', 'Maracujá': 'Frutas', 'Mamão': 'Frutas', 'Jabuticaba': 'Frutas', 'Romã': 'Frutas', 'Amora': 'Frutas', 'Pitanga': 'Frutas', 'Graviola': 'Frutas', 'Carambola': 'Frutas', 'Nectarina': 'Frutas', 'Cereja': 'Frutas', 'Lichia': 'Frutas', 'Framboesa': 'Frutas', 'Abacate': 'Frutas', 'Jaca': 'Frutas', 'Tamarindo': 'Frutas', 'Caqui': 'Frutas', 'Tangerina': 'Frutas', 'Coco': 'Frutas', 'Mirtilo': 'Frutas', 'Fruta do Conde': 'Frutas', 'Cambuci': 'Frutas', 'Mangostão': 'Frutas', 'Araçá': 'Frutas', 'Seriguela': 'Frutas', 'Uvaia': 'Frutas', 'Buriti': 'Frutas', 'Pitaya': 'Frutas', 'Cambucá': 'Frutas', 'Cupuaçu': 'Frutas', 'Açaí': 'Frutas', 'Physalis': 'Frutas', 'João': 'Nomes Comuns', 'Maria': 'Nomes Comuns', 'Pedro': 'Nomes Comuns', 'Ana': 'Nomes Comuns', 'Lucas': 'Nomes Comuns', 'Júlia': 'Nomes Comuns', 'Gabriel': 'Nomes Comuns', 'Beatriz': 'Nomes Comuns', 'Miguel': 'Nomes Comuns', 'Alice': 'Nomes Comuns', 'Arthur': 'Nomes Comuns', 'Laura': 'Nomes Comuns', 'Davi': 'Nomes Comuns', 'Helena': 'Nomes Comuns', 'Matheus': 'Nomes Comuns', 'Sofia': 'Nomes Comuns', 'Rafael': 'Nomes Comuns', 'Valentina': 'Nomes Comuns', 'Guilherme': 'Nomes Comuns', 'Isabella': 'Nomes Comuns', 'Enzo': 'Nomes Comuns', 'Luiza': 'Nomes Comuns', 'Leonardo': 'Nomes Comuns', 'Lívia': 'Nomes Comuns', 'Gustavo': 'Nomes Comuns', 'Giovanna': 'Nomes Comuns', 'Bernardo': 'Nomes Comuns', 'Emanuelly': 'Nomes Comuns', 'Henrique': 'Nomes Comuns', 'Clara': 'Nomes Comuns', 'Samuel': 'Nomes Comuns', 'Antonella': 'Nomes Comuns', 'Felipe': 'Nomes Comuns', 'Yasmin': 'Nomes Comuns', 'Vinícius': 'Nomes Comuns', 'Larissa': 'Nomes Comuns', 'Daniel': 'Nomes Comuns', 'Mariana': 'Nomes Comuns', 'Eduardo': 'Nomes Comuns', 'Gabriela': 'Nomes Comuns', 'Lorenzo': 'Nomes Comuns', 'Sara': 'Nomes Comuns', 'Murilo': 'Nomes Comuns', 'Melissa': 'Nomes Comuns', 'Theo': 'Nomes Comuns', 'Heloísa': 'Nomes Comuns', 'Heitor': 'Nomes Comuns', 'Rafaela': 'Nomes Comuns', 'Isaac': 'Nomes Comuns', 'Game of Thrones': 'Séries Famosas', 'Breaking Bad': 'Séries Famosas', 'Friends': 'Séries Famosas', 'Stranger Things': 'Séries Famosas', 'The Big Bang Theory': 'Séries Famosas', 'The Walking Dead': 'Séries Famosas', "Grey's Anatomy": 'Séries Famosas', 'The Office': 'Séries Famosas', 'House of Cards': 'Séries Famosas', 'Vikings': 'Séries Famosas', 'Sherlock': 'Séries Famosas', 'True Detective': 'Séries Famosas', 'The Mandalorian': 'Séries Famosas', 'Black Mirror': 'Séries Famosas', 'Westworld': 'Séries Famosas', 'The Crown': 'Séries Famosas', 'Narcos': 'Séries Famosas', 'Peaky Blinders': 'Séries Famosas', 'Sons of Anarchy': 'Séries Famosas', 'Dexter': 'Séries Famosas', 'Lost': 'Séries Famosas', 'House': 'Séries Famosas', 'How I Met Your Mother': 'Séries Famosas', 'Suits': 'Séries Famosas', '24 Horas': 'Séries Famosas', 'Prison Break': 'Séries Famosas', 'Mad Men': 'Séries Famosas', 'Homeland': 'Séries Famosas', 'Arrow': 'Séries Famosas', 'Supernatural': 'Séries Famosas', 'Buffy the Vampire Slayer': 'Séries Famosas', 'Smallville': 'Séries Famosas', 'Two and a Half Men': 'Séries Famosas', 'ER': 'Séries Famosas', 'CSI: Crime Scene Investigation': 'Séries Famosas', 'NCIS': 'Séries Famosas', 'The Sopranos': 'Séries Famosas', 'Seinfeld': 'Séries Famosas', 'The X-Files': 'Séries Famosas', "The Handmaid's Tale": 'Séries Famosas', 'Better Call Saul': 'Séries Famosas', 'Fargo': 'Séries Famosas', 'Parks and Recreation': 'Séries Famosas', 'Lucifer': 'Séries Famosas', 'Money Heist (La Casa de Papel)': 'Séries Famosas', 'Rick and Morty': 'Séries Famosas', 'Brooklyn Nine-Nine': 'Séries Famosas', 'The Witcher': 'Séries Famosas', 'Ozark': 'Séries Famosas'}
    palavra1, grupo = random.choice(list(dicionário_palavras.items()))
    letras_erradas = []
    tentativas = int
    
    palavra_sem_acento = substituir(palavra1)

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

    m = letras_palavra(palavra1)
    print(grupo)

    while tentativas > 0:
        if '_' not in m:
            print(f'----------\nVocê ganhou! A resposta é {palavra1}.')
            return
        print('\n----------\n')
        print(' '.join(m))
        print(f'Você ainda tem {tentativas} tentativas.')
        print('Letras erradas:',' '.join(letras_erradas))
        letra = input('Insira uma letra: ')
        if len(letra) != 1 or letra == 'â' or letra == 'ã' or letra == 'é' or letra == 'ê' or letra == 'í' or letra == 'î' or letra == 'ó' or letra =='ô' or letra == 'ú' or letra == 'û':
            continue
        elif letra.upper() in letras_erradas:
            continue
        elif letra.lower() in palavra_sem_acento.lower():
            print(f'A letra "{letra.upper()}" está na palavra!')
            for i in range(0,len(palavra1)):
                if letra.lower() == palavra_sem_acento.lower()[i]:
                    m[i] = letra.upper()
                else:
                    continue
        elif letra.lower() not in palavra_sem_acento.lower():
            tentativas -= 1
            letras_erradas.append(letra.upper())
            print(f'A letra "{letra.upper()}" não está na palavra!')
            if tentativas == 0:
                print(f'----------\nVocê perdeu! A resposta era {palavra1}')
        
if __name__ == "__main__":
    game()
    print('Até a próxima!')