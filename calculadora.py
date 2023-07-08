OUTPUT_TEMPLATE = "RESULTADO:{}"
while True:
    template = ("=============CALCULADORA===============\n"
                "1 - Soma\n"
                "2 - Subtração\n"
                "3 = Multiplicação\n"
                "4 = Divisão\n"
                "5 = SAIR\n"
                "======================================")
    print(template)
    operacao = float(input("Digite a operação desejada:"))

    if operacao == 5:
     print("Obrigada por usar nossa calculadora!")
     quit()
    
    num1 = float(input("Primeiro numero:")) 
    num2 = float(input("Segundo numero:"))

    if operacao == 1:
     print(OUTPUT_TEMPLATE.format(num1 + num2))

    elif operacao == 2:
     print(OUTPUT_TEMPLATE.format(num1 - num2))

    elif operacao == 3:
     print(OUTPUT_TEMPLATE.format(num1 * num2))

    elif operacao == 4:
     print(OUTPUT_TEMPLATE.format(num1 / num2))

    