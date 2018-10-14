#!/usr/bin/env python

NOMBRE_ARCHIVO_DE_ENTRADA = "a.in"
NOMBRE_ARCHIVO_DE_SALIDA = "outcome.out"


def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")

def kenTroncoMasGrande(troncosKen, troncoNaomi):
	for x in xrange(0, len(troncosKen)):
		if troncosKen[x] > troncoNaomi: return x
	return -1
	
def resuelve(cantidadDeTroncos, troncosNaomi, troncosKen):
	troncosNaomi.sort()
	troncosKen.sort()
	
	copiaNaomi = list(troncosNaomi)
	copiaKen = list(troncosKen)
	
	puntosNaomiDeceitful = 0
	puntosNaomiNormal = 0
	
	troncosQueFaltanJugar = cantidadDeTroncos
	
	while troncosQueFaltanJugar > 0:
		if troncosNaomi[troncosQueFaltanJugar-1] > troncosKen[troncosQueFaltanJugar-1]:
			troncosNaomi.pop()
			troncosKen.pop()
			puntosNaomiDeceitful += 1
		else:
			troncosKen.pop()
			troncosNaomi.pop(0)
		troncosQueFaltanJugar -= 1
	
	troncosQueFaltanJugar = cantidadDeTroncos
	troncosNaomi = copiaNaomi
	troncosKen = copiaKen
	
	while troncosQueFaltanJugar > 0:
		indiceTroncoKenMayorQueTroncoNaomi = kenTroncoMasGrande(troncosKen, troncosNaomi[0])
		if (indiceTroncoKenMayorQueTroncoNaomi == -1):
			puntosNaomiNormal += 1
			troncosKen.pop(0)
			troncosNaomi.pop(0)
		else:
			troncosKen.pop(indiceTroncoKenMayorQueTroncoNaomi)
			troncosNaomi.pop(0)
		
		troncosQueFaltanJugar -= 1
		
	return str(puntosNaomiDeceitful)+" "+str(puntosNaomiNormal)
	
def lector():
	entrada = open(NOMBRE_ARCHIVO_DE_ENTRADA, 'r')
	
	for caso in xrange(int(entrada.readline())):
		cantidadDeTroncos = int(entrada.readline())
		troncosNaomi = entrada.readline().split()
		troncosKen = entrada.readline().split()
		
		for x in xrange(cantidadDeTroncos):
			troncosNaomi[x] = float(troncosNaomi[x])
			troncosKen[x] = float(troncosKen[x])
		
		sol = resuelve(cantidadDeTroncos, troncosNaomi, troncosKen)
		imprime(caso+1, sol)

def main():
	lector()

salida = open(NOMBRE_ARCHIVO_DE_SALIDA, 'w')
main()
salida.close()
