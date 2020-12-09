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

						Siempre podrás salir de la partida cerrando la pestaña o escribiendo "exit" o "salir" en el momento el 
						que se te pida realizar una decisión.

						""")

			enter = input("Presiona enter para continuar: ")



			while (enter == ''):
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

				#La variable "res1" es la del tutrorial.
				res1 = input('Elige una opción: ')

				if (res1 == '1'):
					print('\n*Entras a la habitación del asesino y te apuñala hasta la muerte.* ')
					input("\nHas muerto, presiona enter para volver a intentarlo:")
				elif (res1 == '2'):
					print('\n*Entras a la habitación del horno y te quemas hasta morir.* ')
					input("\nHas muerto, presiona enter para volver a intentarlo:")
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
		while (option == 'b'):
			print ("""

					Estás en una fiesta, cuando de repente se apagan las luces y de las 10 personas en total
					aparece una muerta, Su nombre era Diego. Las otras 8 personas y tu se ven desconcertados, muchos 	
					ponen su mirada en ti pero pronto pierden el interés, se enfocan en alguien en especial, el típico
					bully de clase. El Bryant. El chico con peor reputación en la escuela. Esto debido a su mala relación
					con todos, es una persona desagrable para los demás por sus actos. Se defendió diciendo que era una
					estupides pensar que el hiciese algo así, sin embargo la multitud no detiene sus acusaciones.

					Que harás?

				""")
			#La variable "res2" divide el a-)Tener una buena impresión de ti, b-)hacerte enemigo de el, o c-)Tener una relación neutra.
			res2 = input('''

				a-) Defender a Bryant y mentir al decir que lo estuviste con el todo el tiempo.
				b-) Acusarlo también.
				c-) No hacer nada y dejar que la multitud se encarge. Al final, no es sunto tuyo.

				Elige: ''')

			if res2 == 'a':
				print("""

					Les dices a todos que Bryant estuvo contigo todo el rato, la gente te mira por un momento pero luego
					pierden el interés y se alejan de la zona quedando solo tú y Bryant.

					Bryant te mira pero no se atreve a decir nada.

					""")
				#La variable "res3" se divide en a-) Iniciar una conversacion y posible amistad, b-) Dejarle solo una buena impresión.
				res3 = input("""

					a-)Hablar.
					b-)No decir nada. Ni lo conoces.

					Eige: """)
				if res3 == "a":
					print("""

						Le preguntas que Cómo está. Se mira reacio a responder, sin embargo te dice que está bien. Ves que no
						quiere seguir respondiendo tus preguntas, así que decides salir de la habitación.

						Llegas a el salón 2 personas de la fiesta deciden llamar a la policia, sin embargo algo en los móviles va mal,
						no hay señal. Tu y dos personas mas deciden ir a revisar el teléfono fijo para comprobar si funciona. Al
						llegar se confirma, por algún motivo los medios de comunicación con el exterior no están disponibles.

						Las personas intentan salir por la puerta sin embargo no abre. Ya cansados deciden salir por la ventan, pero
						tampoco abren. La gente ya empieza a desesperar, sin embargo una chica, llamada Leila pone en calma a todo el
						mundo diciendo que solo es cuestión de tiempo para que llegue la señal o para que alguien llegue a la casa.
						Todos deciden abandonar la zona en la que se encuentran los fallecidos.

						La gente se siente mas calmada y decide esperar. En eso Leila se acerca a ti y te dice que sabe que no estuviste
						con Bryant y que mentiste para protegerlo. Te preguntal el por que lo hiciste.

						Cómo responderás?

						""")

					res3_1 = input("""

					a-) Le dices que no sabe de lo que está hablando, que está equivocada.
					b-) No le respones. No estas obligado.
					c-) Le dices que tiene razón pero que lo dijiste porque sabes que no fue el.

					""")
				if res3 == 'b':
					print("""

						Decides no hablarle y sales de la habitación.

						Llegas a el salón 2 personas de la fiesta deciden llamar a la policia, sin embargo algo en los móviles
						va mal, no hay señal. Tu y dos personas mas deciden ir a revisar el teléfono fijo para comprobar si
						funciona. Al llegar se confirma, por algún motivo los medios de comunicación con el exterior no están
						disponibles.

						Las personas intentan salir por la puerta sin embargo no abre. Ya cansados deciden salir por la ventan, pero
						tampoco abren. La gente ya empieza a desesperar, sin embargo una chica, llamada Leila pone en calma a todo el
						mundo diciendo que solo es cuestión de tiempo para que llegue la señal o para que alguien llegue a la casa.
						Todos deciden abandonar la zona en la que se encuentran los fallecidos.

						La gente se siente mas calmada y decide esperar. Tu te sientas en un sodá cercano a mirar el móvil.


						""")


			elif res2 == 'b':
				print("""

					Acusas a Bryant junto con los demás y deciden encerrarlo en una habitación como medida de prevención.(Bryant lo recordará)
					2 personas de la fiesta deciden llamar a la policia, sin embargo algo en los móviles va mal, no hay señal. Tu
					y dos personas mas deciden ir a revisar el teléfono fijo para comprobar si funciona. Al llegar se confirma, por
					algún motivo los medios de comunicación con el exterior no están disponibles.

					Las personas intentan salir por la puerta sin embargo no abre. Ya cansados deciden salir por la ventan, pero
					tampoco abren. La gente ya empieza a desesperar, sin embargo una chica, llamada Leila pone en calma a todo el
					mundo diciendo que solo es cuestión de tiempo para que llegue la señal o para que alguien llegue a la casa.
					Todos deciden abandonar la zona en la que se encuentran los fallecidos.

					La gente se siente mas calmada y decide esperar. Tu te sientas en un sofá cercano a mirar el móvil.

					""")

				

			else:
				print("Elige una opción correcta.")

		else:
			print("Elige una opcion correcta. ")
			break

	if (option == 'd'):
		break