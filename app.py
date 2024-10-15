# Solicitar peso e altura do usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Exibir o valor do IMC
print(f"Seu IMC é: {imc:.2f}")

# Diagnóstico baseado no valor do IMC
if imc < 18.5:
    print("Diagnóstico: Abaixo do peso")
elif imc < 24.9:
    print("Diagnóstico: Peso normal")
elif imc < 29.9:
    print("Diagnóstico: Sobrepeso")
elif imc < 34.9:
    print("Diagnóstico: Obesidade grau I")
elif imc < 39.9:
    print("Diagnóstico: Obesidade grau II")
else:
    print("Diagnóstico: Obesidade grau III")

