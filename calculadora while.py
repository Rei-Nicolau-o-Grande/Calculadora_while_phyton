while True:
    num1 = input("Digite um numero: ")
    num2 = input("Digite outro numero: ")
    operador = input("Escolha o operador (ex: +, -, *, /): ")

    if  not num1.isnumeric() or not num2.isnumeric(): # Verificar quando o usuario vai digitar um numero
        print("Erro Digite um numero.")
        continue

    num1 = int(num1) # transformando a variavel de boolean para inteiro
    num2 = int(num2) # # transformando a variavel de boolean para inteiro

    if operador == "+":
        print(f"Resultado: {num1 + num2}")
    elif operador == "-":
        print(f"Resultado: {num1 - num2}")
    elif operador == "*":
        print(f"Resultado: {num1 * num2}")
    elif operador == "/":
        print(f"Resultado: {num1 // num2}")
    else:
        print("Vc não digitou nenhum dos operadores (+, -, *, /)")

    sair = input("Vc deseja continuar S(im) ou N(ão) ?")

    if sair == "n":
        break
