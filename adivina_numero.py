#---------------------------ADIVINA EL NUMERO--------------------------#
# 30/05/2021
# Santiago, Chile
# Eddie Casañas
#-----------------------------------------------------------------------#
import random as rd

def jugador():
	nombre = input("\nDame tu nombre: ")
	print("\nBienvenido " + nombre.capitalize() + ". Adivina un numero del 1 al 20")
	print("Tienes 5 intentos")
	print("Presione el numero cero (0) en cualquier momento para salir")
	pc = rd.randint(1,20)
	n = 0
	while n < 5:
		print("\nINTENTO #" + str(n + 1))
		try:
			opcion_j = int(input("\nDame un numero del 1 al 20: "))
		except:
			print("Por favor, ingrese un numero valido")
			continue
		else:
			if opcion_j == 0:
				break
			elif opcion_j not in range(1,21):
				print("Por favor, ingrese un numero entre el rango solicitado")
				continue
			elif opcion_j < pc:
				n += 1
				if n != 5:
					print("Un poco bajo. Intentalo de nuevo")
				
				continue
			elif opcion_j > pc:
				n += 1
				if n != 5:
					print("Un poco alto. Intentalo de nuevo")
				continue
			if opcion_j == pc:
				break
	if opcion_j == 0:
		pass
	elif opcion_j == pc:
		print("\nFelicidades, adivinaste el numero en " + str(n + 1) + " intentos")
	else:
		print("\nNo adivinaste el numero. El numero correcto era " + str(pc))

def pregunta():
	print("\n(1): Jugar")
	print("(2): Salir")
	opcion = input().lower().strip()
	return opcion

while True:
	opcion = pregunta()
	if opcion == "1":
		jugador()
	elif opcion == "2":
		break
	else:
		print("Ingrese una opcion valida")