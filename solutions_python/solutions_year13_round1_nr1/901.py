#!/usr/bin/env python



salida = open("outcome.out", 'w')



def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")


def calcular_area_anillo(radio_menor):
	return ( 2*radio_menor +1 )
	
def resuelve(r, t):
	superficie_que_se_puede_pintar = t
	
	radio = r
	
	cantidad_de_anillos_posibles = 0
	while True:

		superficie_que_se_puede_pintar -= calcular_area_anillo(radio)
		
		if superficie_que_se_puede_pintar < 0: break
		
		cantidad_de_anillos_posibles += 1
		radio += 2
	
	return cantidad_de_anillos_posibles


def lector():
	entrada = open("A-small-attempt1.in", 'r')
	
	for caso in xrange(int(entrada.readline())):
		#crea tablero
		
		r, t = entrada.readline().split()
		r, t = int(r), int(t)
		
		imprime(caso+1, resuelve(r,t))
	

def main():
	lector()

main()
salida.close()










