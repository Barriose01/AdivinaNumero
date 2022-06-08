#---------------------------ADIVINA EL NUMERO--------------------------#
# 30/05/2021
# Santiago, Chile
# Eddie Casañas

import random as rd


def jugador():
	nombre = input("\nDame tu nombre: ")
	print("Bienvenido " + nombre.capitalize() + ". Adivina un numero del 1 al 20")
	print("Tienes 5 intentos")
	pc = rd.randint(1,20)
	
	n = 0
	while n < 5:
		
		try:
			opcion_j = int(input("\nDame un numero del 1 al 20: "))
		except:
			print("Por favor, ingrese un numero valido")
			continue
		else:
		
			if opcion_j not in range(1,21):
				print("Por favor, ingrese un numero entre el rango solicitado")
				continue
			
			elif opcion_j < pc:
				print("Un poco bajo. Intentalo de nuevo")
				n += 1
				continue
			elif opcion_j > pc:
				print("Un poco alto. Intentalo de nuevo")
				n += 1
				continue
			if opcion_j == pc:
				break
			
	if opcion_j == pc:
		
		print("\nFelicidades, adivinaste el numero en " + str(n + 1) + " intentos")
		pregunta()
		
	else:
		print("\nNo adivinaste el numero. El numero correcto era " + str(pc))
		n = 0
		pregunta()

def pregunta():
	pregunta = input("¿Deseas volver a jugar? (y/n): ")
	if pregunta.strip().lower() == "y":
		jugador()
	else:
		pass
			
			
jugador()
