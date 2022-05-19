import random
from re import A

def jogar():

    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("\nDigite uma letra... \n")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)
    print("\nFim do jogo!\n")

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def mensagem_perdedor(palavra_secreta):
    print("\nVocê foi ENFORCADO!\n")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________ ")
    print("    /               \ ")
    print("   /                 \ ")
    print("/\/                   \/\ ")
    print("\ |   XXXX     XXXX   | / ")
    print(" \|   XXXX     XXXX   |/ ")
    print("  |   XXX       XXX   | ")
    print("  |                   | ")
    print("  \__       X       __/ ")
    print("    |\     XXX     /| ")
    print("   /| I           I |\ ")
    print("  / | I I I I I I I | \ ")
    print(" / /|  I I I I I I  |\ \ ")
    print(" \/ \_             _/ \/ ")
    print("      \_         _/ ")
    print("        \_______/ ")

def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ____________     ")
    print("      '._==_==_==_.'    ")
    print("      .-\\:      /-.    ")
    print("     | (|:.      |) |    ")
    print("      '-|:.      |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
