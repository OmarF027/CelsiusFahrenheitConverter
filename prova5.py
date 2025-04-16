domanda = input("Fahrenheit o Celsius? (F/C): ")
domanda2 = int(input("Quanti gradi ci sono? "))
if domanda == "F":
    gradi_celsius = (domanda2 - 32) * 5/9
    print("La temperatura in Celsius è: " + str(gradi_celsius))
    gradi_kelvin = gradi_celsius + 273.15
    print("La temperatura in Kelvin è: " + str(gradi_kelvin))
elif domanda == "C":
    gradi_fahrenheit = (domanda2 * 9/5) + 32
    print("La temperatura in Fahrenheit è: " + str(gradi_fahrenheit))
    gradi_kelvin = domanda2 + 273.15
    print("La temperatura in Kelvin è: " + str(gradi_kelvin))
else:
    print("Errore: inserire F o C")