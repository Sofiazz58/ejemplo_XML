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

def contar_radares_por_carretera(arbol,carretera):
	numero=arbol.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)'%carretera)
	latitud=arbol.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()'%carretera)
	longitud=arbol.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'%carretera)
	info=[numero,latitud,longitud]
	return info


from xml.dom import minidom 
docXML = minidom.parse("radares.xml")

def lista_provincias(arbol):
    	nombres = arbol.xpath('//nombre/text()')	
	return nombres

def lista_radares(arbol):
    	cantidad = arbol.xpath('//cantidad/text()')
	return cantidad

def lista_provincia_total_radares(arbol):
    	lista=[]
	nombres = arbol.xpath('//nombre/text()')
	for provincia in arbol.xpath('//provincia'):
		radares=radares.xpath('count(./radares/radares)')	
		lista.append(int(radares))
	return zip(nombres,lista)


def carretera(prov,arbol):
    	nombres = arbol.xpath('/lista/carretera[nombre="%s"]//provincia/text()'%prov)
	return nombres

#LISTAMENU

for nombre in lista_provincias('arbol'):
	print (nombre)
 
for nombre in lista_radares('arbol'):
    print (nombre)
    
for nombre ,total in 'lista_provincias_total_radares'('arbol'):
    	print (nombre,total)
     
for nombre in carretera ("N-320")('arbol'):
    	print (nombre)
    

