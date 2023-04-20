print("________________________________")
print("Bem vindo no jogo de Adivinhacão")
print("________________________________")

numero_secreto = 13
total_de_tentativas = 3

while(total_de_tentativas > 0):
    palpite = input("Digite seu numero:")
    print("voce digitou:","\n" + palpite)
    chute = int(palpite)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("acertou")
        break
    else:
        if(maior):
            print("chutou alto, bateu na trave")
        elif(menor):
            print("chutou baixo demais")

    total_de_tentativas -= 1

print("fim de jogo")
