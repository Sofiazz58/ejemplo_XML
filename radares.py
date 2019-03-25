from lxml import etree
arbol = etree.parse('radares.xml')

while True:
	print()
	print("1.Mostrar el nombre de las provincias de las que tenemos información sobre radares.")
	print("2.Mostrar la cantidad de radares de los que tenemos información.")
	print("3.Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.")
	print("4.Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.")
	print("5.Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap para ver donde está el radar).")
	print("0.Salir")
	print()
	opcion=int(input("Elige opción: "))
	print()

# Opción para despedir el programa
	if opcion == 0:
		print()
		print("Adiós!")
		print()
		break;

	elif opcion == 1:
		print("OK")

# Opción de error de opción		    
	else:
		print()
		print("Error de opción")
		print()