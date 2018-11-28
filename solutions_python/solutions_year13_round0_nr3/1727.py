#!/usr/bin/env python



salida = open("salida.out", 'w')



def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	
	
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")

def es_palindromo(numero):
	numeroString = str(numero)
	return numeroString == numeroString[::-1]
	
def evalua_fair_and_square(minimo, maximo):
	valorMaximoAEvaluar = maximo**(0.5) #Cualquier cuadrado mayor a valorMaximoAEvaluar se va del limite
	
	fairAndSquareNumbers = 0
	
	num = 1
	while num <= valorMaximoAEvaluar:
		if es_palindromo(num):
			cuadradoDeNum = num**2
			if (cuadradoDeNum < minimo): 
				num += 1
				continue
			if es_palindromo(cuadradoDeNum):
				fairAndSquareNumbers += 1
		num += 1
		
	
	return fairAndSquareNumbers
	
def evalua_todos(maximo):
	valorMaximoAEvaluar = maximo**(0.5) #Cualquier cuadrado mayor a valorMaximoAEvaluar se va del limite
	
	dic = {}
	
	num = 1
	while num <= valorMaximoAEvaluar:
		if es_palindromo(num):
			cuadradoDeNum = num**2
			if es_palindromo(cuadradoDeNum):
				dic[cuadradoDeNum] = None
		num += 1
		
	
	return dic
	
def lector():
	entrada = open("a.in", 'r')
	
	for numeroProblema in xrange(int(entrada.readline())):
		#obtiene A y B
		A, B = entrada.readline().split()
		A, B = int(A), int(B)
		
		cantidad = evalua_fair_and_square(A,B)
		
			
		imprime(numeroProblema+1, cantidad)
	

def main():
	lector()

main()
salida.close()










