# Juego de acertijo

print("""

	Bienvenido a un juego, a mi juego. Un acertijo en el cual
	tendrás que responder a las preguntas correctamente.

	Ten en cuenta que el nombre que ingreses será el que 
	tendrás a lo largo de todo el juego.
	""")

name = input("Cómo te llamas? ")

while True:


	print("---------------------------------------------\nOpciones\n a-) Tutorial \n b-) Jugar \n c-) Cambiar nombre \n d-) Salir")

	option = input("\n Hola {0}. Elige una opción: ".format(name))

	while True:


		if (option == 'a'):
			print("""
				               --------------------------------------------------------------------------------------
						Este es un juego en el cual se te pondran en situaciones en las cuales tendrás que
						responder correctamente para hallar al asesino, pero ten cuidado porque puedes 
						morir si eliges una respuesta mal. Bien pasemos a un ejemplo que no tiene que ver
						con la historia original, pero que servirá para entender la mecánica de juego.

						""")

			enter = input("Presiona enter para continuar: ")
			if (enter == ''):
				print('''
						---------------------------------------------------------------------------------------
				         	En una habitacion hay tres puertas. En la primera hay un asesino serial esperando para
				         	matarte, en la segunda es un horno prendido, y en la tercera un leon que no ha comido 
				         	por 3 meses. Cual eliges?

				         	1-)Asesino
				         	2-)Horno
				         	3-)León <--- Esta es la opción correcta debido a que un león que no ha comido
				         	             por todo ese tiempo estaría muerto. Si en este caso eliges la 
				         	             opción 3 pasas a la siguiente fase, sin embargo si eliges una 
				         	             opción incorrecta correras el peligro de ser asesinado. A ver 
				         	             intenta elegir una opción.

							''')
				res1 = input('Elige una opción: ')

				if (res1 == '1'):
					print('\n*Entras a la habitación del asesino y te apuñala hasta la muerte.* ')
					input("\nHas muerto, presiona enter para volver a intentarlo:")
				elif (res1 == '2'):
					print('\n*Entras a la habitación del horno y te quemas hasta morir.* ')
				elif (res1 == '3'):
					print('''

						Bien. Parece que has entendido de que va. Ahora Para empezar
						el juego elige la opcion 'b'.


						''')
					break
		
				else:
					print('Elige una opción correcta. ')


		elif (option == 'c'):
			print('''

	Ten en cuenta que el nombre que ingreses será el que 
	tendrás a lo largo de todo el juego. 

				''')
			name = input("\n Cómo quieres que te llame ahora? ")
			print('\n Nombre cambiado con éxito.')
			break

		elif (option == 'd'):
			break

		else:
			print("Elige una opcion correcta. ")
			break

		while (option == 'b'):
			print('''

						Estás en una fiesta, cuando de repente se apagan las luces y de las 10 personas en total
						aparece una muerta, Su nombre era Diego. Las otras 8 personas y tu se ven desconcertados, muchos 
						ponen tu mirada en ti pero pronto pierden el interés, se enfocan en alguien en especial, el típico
						bully de clase. el Bryant. El chico con peor reputación en la escuela. 

						Obviamente se defendió diciendo que era una estupides pensar que el hiciese algo así 

					''')

	if (option == 'd'):
		break