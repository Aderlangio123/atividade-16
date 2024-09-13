# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

peso = float(input("digite seu peso corporal! : "))
altura = float(input("digite sua altura! : "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"seu imc é {imc}, voce está abaixo do peso!")

elif imc >=18.5 and imc < 25:
    print(f"seu imc é {imc}, voce está com peso peso normal")

elif imc >= 25 and imc < 30:
    print(f"seu imc é {imc}, voce está com sobrepeso")

elif imc >=30 :
    print(f"seu imc é {imc}, voce está com obesidade!!!!!")
    