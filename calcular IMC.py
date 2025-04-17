def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar dados do usuário 
peso = float(input("Digite o seu peso em kg: "))  
altura = float(input("Digite a sua altura em metros: "))  

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Exibir o resultado
print(f"O seu IMC é {imc:.2f}")

# Classificar o IMC corretamente
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso ideal")
elif 25.0 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obeso")
elif 35 <= imc < 39.9:
    print("Obesidade Severa")
elif imc >= 40:  # Alterei para garantir que essa condição só seja atingida para valores altos
    print("Obesidade Mórbida")

# Manter a janela aberta até o usuário pressionar Enter
input("Pressione Enter para fechar...")

