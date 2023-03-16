# Piedra, Papel o Tijeras
import random
print("=====================================================================")
print("===================== Piedra,Papel o Tijera =========================")
print("=====================================================================")
print(' Ingrese 1 para Piedra')
print(' Ingrese 2 para Papel')
print(' Ingrese 3 para Tijeras')

print('=================================================================')

# input

machine = random.randint(1,3)

eleccion = int(input(' Ingrese un numero del 1 al 3 : '))

print('=================================================================')

print('Tú')   

print('=')
if eleccion==1:
    print(' Piedra')
elif eleccion==2:
    print(' Papel')
elif eleccion==3:
    print(' Tijeras')
else:
    print('Ingrese un numero entre 1 y 3')

print('=================================================================')

print('Maquina')

print('=')

if machine==1:
    print(' Piedra')
elif machine==2:
    print(' Papel')
elif machine==3:
    print(' Tijeras')
else:
    print(' Ingrese un numero entre 1 y 3')

# output


if eleccion==2 and machine==1:
    rta=(' Ganaste')
elif eleccion==1 and machine==3:
    rta=('Ganaste')
elif eleccion==2 and machine==2:
    rta=('Empate')
elif eleccion==2 and machine==3:
    rta=('Perdiste')
elif eleccion==3 and machine==3:
    rta=('Empate')
elif eleccion==1 and machine==1:
    rta=('Empate')
elif eleccion==3 and machine==1:
    rta=('Perdiste')
elif eleccion==3 and machine==2:
    rta=('Ganaste')

    

else:
    rta=(' Perdiste')

print('=================================================================')

print(rta)