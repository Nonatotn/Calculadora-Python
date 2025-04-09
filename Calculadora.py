def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b if b != 0 else "Erro: Divisão por zero"

def divisao_inteira(a, b):
    return a // b if b != 0 else "Erro: Divisão por zero"

def modulo(a, b):
    return a % b if b != 0 else "Erro: Divisão por zero"

def exponenciacao(a, b):
    return a ** b

while True:
    print("\nSelecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Divisão inteira")
    print("6 - Módulo (resto)")
    print("7 - Exponenciação")
    print("0 - Sair")
    
    opcao = input("Informe o número da operação: ")
    
    if opcao == "0":
        print("Encerrando a calculadora... Obrigado por usar!")
        break
    
    if opcao not in {"1", "2", "3", "4", "5", "6", "7"}:
        print("Opção inválida! Tente novamente.")
        continue
    
    try:
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))
    except ValueError:
        print("Entrada inválida! Tente novamente.")
        continue
    
    match opcao:
        case "1":
            resultado = soma(num1, num2)
            operacao = "Soma"
        case "2":
            resultado = subtracao(num1, num2)
            operacao = "Subtração"
        case "3":
            resultado = multiplicacao(num1, num2)
            operacao = "Multiplicação"
        case "4":
            resultado = divisao(num1, num2)
            operacao = "Divisão"
        case "5":
            resultado = divisao_inteira(num1, num2)
            operacao = "Divisão inteira"
        case "6":
            resultado = modulo(num1, num2)
            operacao = "Módulo"
        case "7":
            resultado = exponenciacao(num1, num2)
            operacao = "Exponenciação"
    
    print(f"Resultado da {operacao}: {resultado}")