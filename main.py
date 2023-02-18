from Imc import Imc

def main():

    weight = float(input('Type your weight in kg: '))
    height = float(input('Type your height in meters: '))
    quantity = float(input('Type your height in meters: '))

    instanceImc = Imc(height, weight)
    if quantity > 0:
        instanceImc.pacoca = 'Tem paçoca.'

    imc = instanceImc.calculate_imc()
    print('Your body mass index is:', imc)

    if instanceImc.pacoca != None:
        print('Comeu muita paçoca então o imc é vezes 2:', imc * 2)

    print('', instanceImc.pacoca)

    if imc < 18.5:
        print('You are under weight')
    elif 18.5 <= imc <= 24.9:
        print('You are on ideal weighe')
    elif 25.0 <= imc <= 29.9:
        print('You are overweight')
    else:
        print('You are obese')

if __name__ == '__main__':
    main()