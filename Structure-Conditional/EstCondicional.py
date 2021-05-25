import os, sys

focos_verdes = 0
focos_blancos = 0
focos_rojos = 0
n = int (input ('Ingresa el valor de n: '))
for i in range (1, n + 1):
    print ('PROCESO ' + repr (i))
    print ('Selecciona el valor de color.')
    print ('\t1.- verde')
    print ('\t2.- blanco')
    print ('\t3.- rojo')
    sys.stdout.write ('\t')
    color = 0
    while color<1 or color>3:
        color = int (input (': '))
        if color<1 or color>3:
            sys.stdout.write ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
    if color==1:
        focos_verdes=focos_verdes+1
    if color==2:
        focos_blancos=focos_blancos+1
    if color==3:
        focos_rojos=focos_rojos+1
    print ()
print ('Valor de focos verdes: ' + repr (focos_verdes))
print ('Valor de focos blancos: ' + repr (focos_blancos))
print ('Valor de focos rojos: ' + repr (focos_rojos))
os.system ('pause')


import os

total = 0
n = int (input ('Ingresa el valor de n: '))
for i in range (1, n + 1):
    print ('PROCESO ' + repr (i))
    cantidad_01_enero = float (input ('Ingresa el valor de cantidad 01 enero: '))
    cantidad_02_febrero = float (input ('Ingresa el valor de cantidad 02 febrero: '))
    cantidad_03_marzo = float (input ('Ingresa el valor de cantidad 03 marzo: '))
    cantidad_04_abril = float (input ('Ingresa el valor de cantidad 04 abril: '))
    cantidad_05_mayo = float (input ('Ingresa el valor de cantidad 05 mayo: '))
    cantidad_06_junio = float (input ('Ingresa el valor de cantidad 06 junio: '))
    cantidad_07_julio = float (input ('Ingresa el valor de cantidad 07 julio: '))
    cantidad_08_agosto = float (input ('Ingresa el valor de cantidad 08 agosto: '))
    cantidad_09_septiembre = float (input ('Ingresa el valor de cantidad 09 septiembre: '))
    cantidad_10_octubre = float (input ('Ingresa el valor de cantidad 10 octubre: '))
    cantidad_11_noviembre = float (input ('Ingresa el valor de cantidad 11 noviembre: '))
    cantidad_12_diciembre = float (input ('Ingresa el valor de cantidad 12 diciembre: '))
    intereses=total*0.1
    total=total+intereses+cantidad_01_enero+cantidad_02_febrero+cantidad_03_marzo+cantidad_04_abril+cantidad_05_mayo+cantidad_06_junio+cantidad_07_julio+cantidad_08_agosto+cantidad_09_septiembre+cantidad_10_octubre+cantidad_11_noviembre+cantidad_12_diciembre
    inversion_final=total
    print ('Valor de intereses: ' + repr (intereses))
    print ('Valor de inversion final: ' + repr (inversion_final))
    print ()
print ('Valor de total: ' + repr (total))
os.system ('pause')

import os

billetes_de_100 = int (input ('Ingresa el valor de billetes de 100: '))
billetes_de_1000 = int (input ('Ingresa el valor de billetes de 1000: '))
billetes_de_20 = int (input ('Ingresa el valor de billetes de 20: '))
billetes_de_200 = int (input ('Ingresa el valor de billetes de 200: '))
billetes_de_50 = int (input ('Ingresa el valor de billetes de 50: '))
billetes_de_500 = int (input ('Ingresa el valor de billetes de 500: '))
monedas_de_1 = int (input ('Ingresa el valor de monedas de 1: '))
monedas_de_10 = int (input ('Ingresa el valor de monedas de 10: '))
monedas_de_2 = int (input ('Ingresa el valor de monedas de 2: '))
monedas_de_20 = int (input ('Ingresa el valor de monedas de 20: '))
monedas_de_5 = int (input ('Ingresa el valor de monedas de 5: '))
total=billetes_de_1000*1000+billetes_de_500*500+billetes_de_200*200+billetes_de_100*100+billetes_de_50*50+billetes_de_20*20+monedas_de_20*20+monedas_de_10*10+monedas_de_5*5+monedas_de_2*2+monedas_de_1
print ('Valor de total: ' + repr (total))
print ()
os.system ('pause')