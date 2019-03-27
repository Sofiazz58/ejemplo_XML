from lxml import etree
arbol = etree.parse('radares.xml')

def provincias(arbol):
	provincia=arbol.xpath("//NOMBRE/text()")
	return provincia

def contar_radares(arbol):
	numero=arbol.xpath('count(//RADAR)')
	return numero

def provincia_carreteras(arbol,provincia):
	carretera=arbol.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/DENOMINACION/text()'%provincia)
	return carretera

def prov_pasa(arbol,carretera):
	provincias = arbol.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%carretera)
	return provincias

def radares(arbol,carretera):
	punto_ini = arbol.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/PK/text()'%carretera)
	punto_fin = arbol.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_FINAL/PK/text()'%carretera)
	return zip(punto_ini,punto_fin)

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
		print("Provincias con información de radares:")
		print()
		for provincia in provincias(arbol):
			print(provincia)

	elif opcion == 2:
		print("Tenemos",int(contar_radares(arbol)),"radares de los que mostrar información.")
		
	elif opcion == 3:
		lista=[]
		provincia=input("Dime una provincia: ").title()
		for nombre in provincia_carreteras(arbol,provincia):
			if nombre not in lista:
				lista.append(nombre)
		if len(lista) == 0:
			print("No existe la provincia.")
		else:
			for i in lista:
				numero=arbol.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)'%i)
				if numero == 1:
					print("La carretera",i,"tiene",int(numero),"radar")
				else:
					print("La carretera",i,"tiene",int(numero),"radares")

	elif opcion == 4:
		carretera=input("Dime una carretera: ").upper()
		print()
		print("La carretera %s pasa por:" % carretera)
		for provincia in prov_pasa(arbol,carretera):
			if len(provincia)=="0":
				print("NIO")
			else:
				print("si")
				print(provincia)

		print()
		print("Sus radares son: ")
		cont=1
		for punto_ini,punto_fin in radares(arbol,carretera):
			print("Radar número %i: " %cont)
			print("Punto inicial: %s" % punto_ini)
			print("Punto final: %s" % punto_fin)
			print()
			cont=cont+1

# Opción de error de opción		    
	else:
		print()
		print("Error de opción")
		print()