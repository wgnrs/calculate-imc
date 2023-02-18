weight = float(input('Type your wight on kg: '))
height = float(input('Type your height on meters'))

imc = round(weight / (height * 2))

print('Your body mass index is: ', imc)

if imc < 18.5:
    print("You'r under ideal weight")
elif 18.5 <= imc <= 24.0:
    print("You'r on ideal weight")
elif 25.0 <= imc <= 29.9:
    print("You'r overweight")
else:
    print("You'r obese")
