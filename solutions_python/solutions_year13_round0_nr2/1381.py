#!/usr/bin/env python



salida = open("salida.out", 'w')



def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	
	
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")


class Jardin(object):
	def __init__(self, n, m):
		self.jardin = []
		self.n = n
		self.m = m
				
	def imprimir_jardin(self):
		print self.jardin
	
	def agrega_linea(self, linea):
		listaDeNumeros = linea.split()
		for x in xrange(len(listaDeNumeros)): listaDeNumeros[x] = int(listaDeNumeros[x])
		self.jardin.append(listaDeNumeros)
	
	def posicion_tiene_mayor_en_fila(self, x, y):
		hay_mayor = False
		for pos in xrange(self.m):
			if self.jardin[x][pos] > self.jardin[x][y]:
				hay_mayor = True
				return hay_mayor
		return hay_mayor
		
	def posicion_tiene_mayor_en_columna(self, x, y):
		hay_mayor = False
		for pos in xrange(self.n):
			if self.jardin[pos][y] > self.jardin[x][y]:
				hay_mayor = True
				return hay_mayor
		return hay_mayor
		
	def posicion_posible(self, x, y):
		posible = True
		if self.posicion_tiene_mayor_en_columna(x,y) and self.posicion_tiene_mayor_en_fila(x,y):
			posible = False
		return posible
		
		
	def posible(self):
		posible = True
		for x in xrange(self.n):
			for y in xrange(self.m):
				 if not self.posicion_posible(x,y):
					 posible = False
					 return posible
		
		return posible

def lector():
	entrada = open("a.in", 'r')
	
	for numero_de_jardin in xrange(int(entrada.readline())):
		#obtiene n y m
		n, m = entrada.readline().split()
		n, m = int(n), int(m)
		
		#crea jardin
		jardin = Jardin(n,m)
		for x in xrange(n):
			jardin.agrega_linea(entrada.readline())
	
		#evalua
		posible = jardin.posible()
		if posible: posible = "YES"
		else: posible ="NO"
		
		imprime(numero_de_jardin+1, posible)
	

def main():
	lector()

main()
salida.close()










