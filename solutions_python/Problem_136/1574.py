#!/usr/bin/env python

NOMBRE_ARCHIVO_DE_ENTRADA = "a.in"
NOMBRE_ARCHIVO_DE_SALIDA = "outcome.out"


def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")


def cuentaTiempo(cookieAmount, farmProduction, cps, farmAmount):
	return cookieAmount / (cps + farmProduction*farmAmount)

def cuentaTiempoGanar(winAmount, farmProduction, cps, farmAmount):
	return cuentaTiempo(winAmount, farmProduction, cps, farmAmount)
	
def cuentaTiempoSiguienteGranja(farmPrice, farmProduction, cps, farmAmount):
	return cuentaTiempo(farmPrice, farmProduction, cps, farmAmount)
	
def resuelve(farmPrice, farmProduction, winAmount):
	cps = 2 #Cookies per second
	farmAmount = 0
	tiempoEsperandoGranjas = 0
	mejorTiempoParaGanar = cuentaTiempoGanar(winAmount, farmProduction, cps, farmAmount)
	
	while True:
		tiempoEsperandoGranjas += cuentaTiempoSiguienteGranja(farmPrice, farmProduction, cps, farmAmount)
		farmAmount += 1
		
		tiempoParaGanarActual = tiempoEsperandoGranjas + cuentaTiempoGanar(winAmount, farmProduction, cps, farmAmount)
		
		if tiempoParaGanarActual < mejorTiempoParaGanar:
			mejorTiempoParaGanar = tiempoParaGanarActual
		else:
			#print "hola"
			break
			
	#print "Best time: "+str(mejorTiempoParaGanar)
	return mejorTiempoParaGanar
	
def lector():
	entrada = open(NOMBRE_ARCHIVO_DE_ENTRADA, 'r')
	
	for caso in xrange(int(entrada.readline())):
		farmPrice, farmProduction, winAmmount = entrada.readline().split()
		
		farmPrice = float(farmPrice)
		farmProduction = float(farmProduction)
		winAmmount = float(winAmmount)
		
		sol = resuelve(farmPrice, farmProduction, winAmmount)
		imprime(caso+1, sol)

def main():
	lector()

salida = open(NOMBRE_ARCHIVO_DE_SALIDA, 'w')
main()
salida.close()
