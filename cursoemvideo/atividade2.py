peso = float(input('Digite o seu peso'))
altura = float(input('Digite a sua altura'))

imc = peso / (altura ** 2 )
##acima do peso
##dentro do peso
##abaixo do peso
##obesidade morbida
if imc >= 18.5:
    print('Dentro do peso')
    
elif imc < 18.5:
    print('Abaixo do peso')

elif imc > 24.9:
    print('Acima do peso')

else:
    print('Obesidade morbida')