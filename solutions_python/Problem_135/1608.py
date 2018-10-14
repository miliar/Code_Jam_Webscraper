#!/usr/bin/env python

NOMBRE_ARCHIVO_DE_ENTRADA = "a.in"
NOMBRE_ARCHIVO_DE_SALIDA = "outcome.out"


def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")
	
def resuelve(primerArregloCartas, primeraLinea, segundoArregloCartas, segundaLinea):
	posibles = {}
	seguras = {}
	for x in xrange(4):
		posibles[primerArregloCartas[primeraLinea][x]] = True
	for y in xrange(4):
		cartaPosible = segundoArregloCartas[segundaLinea][y]
		if cartaPosible in posibles:
			seguras[cartaPosible] = True
	#print posibles.keys()
	#print seguras
	if len(seguras) == 0: return "Volunteer cheated!"
	if len(seguras) == 1: return str(seguras.keys()[0])
	return "Bad magician!"
	
def leeUnArregloDeCartas(archivo):
		arregloCartas = [[],[],[],[]]
		for row in xrange(4):
			linea = archivo.readline().split()
			for item in linea:
				arregloCartas[row].append(int(item))
		return arregloCartas

def lector():
	entrada = open(NOMBRE_ARCHIVO_DE_ENTRADA, 'r')
	
	for caso in xrange(int(entrada.readline())):
		primeraLinea = int(entrada.readline())-1
		primerArregloCartas = leeUnArregloDeCartas(entrada)
		segundaLinea = int(entrada.readline())-1
		segundoArregloCartas = leeUnArregloDeCartas(entrada)
		
		sol = resuelve(primerArregloCartas, primeraLinea, segundoArregloCartas, segundaLinea)
		imprime(caso+1, sol)

def main():
	lector()

salida = open(NOMBRE_ARCHIVO_DE_SALIDA, 'w')
main()
salida.close()
