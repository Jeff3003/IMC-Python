# Indice_Massa_Corporal
#IMC
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print ( 'Seu IMC é {:.2f}'.format(imc))
if imc <= 18:
    print ('Você está abaixo do peso ideal')
elif imc >= 18.1 and imc <= 25:
        print('Você está no peso ideal')
elif imc >= 25.1 and imc <= 30:
    print ('Você está com sobrepeso')
elif imc >= 30.1 and imc <= 40:
    print ('Você está Obeso')
else:
    print ('VOCÊ ESTÁ COM OBESIDADE MÓRBIDA')
