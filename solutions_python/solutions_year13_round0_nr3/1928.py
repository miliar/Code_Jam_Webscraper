def espalindromo(potencia):
	tam=len(potencia)
	
	if tam==1:
		return True
	elif tam==2:
		if potencia[0]==potencia[-1]:
			return True
	elif potencia[0]!=potencia[-1]:
		return False
	else:
		del potencia[0]
		del potencia[-1]
		return espalindromo(potencia)
	

import sys
import math

if(len(sys.argv) > 1):
	fichero = sys.argv[1]
else: 
	print "Debes indicar el nombre del archivo"

f = open(fichero, "r")
casos=int(f.readline())

i=1
while i<=casos:
	fila1=f.readline()
	datos=fila1.split(' ')
	inicio=int(datos[0])
	fin=int(datos[-1])		
	r=math.sqrt(inicio)
	a=int(math.ceil(r))
	
	numero=0
	potencia=int(a*a)
	while(potencia<=fin and potencia>=inicio):
		if espalindromo(list(str(potencia))) and espalindromo(list(str(a))):		
			numero=numero+1
		a=a+1
		potencia=int(a*a)

	print "Case #%s: %d" % (i,numero)
	i=i+1
