from palavraForca import palavra

letras_usuarios = []
chances = 4
ganhou = False


while True:
    for letra in palavra:
        if letra.lower() in letras_usuarios:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            
    print(f"Você tem {chances} chances!!")
    
    tentativa = input('Escolha a letra da Palavra: ')
    letras_usuarios.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuarios:
            ganhou = False
    if chances == 0 or ganhou:
        
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra er: {palavra}")
else:
    print(f"Você perdeu!! a palavra era: {palavra}")
    