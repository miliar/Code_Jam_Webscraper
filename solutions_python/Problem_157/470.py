#!/usr/bin/env python

NOMBRE_ARCHIVO_DE_ENTRADA = "a.in"
NOMBRE_ARCHIVO_DE_SALIDA = "outcome.out"

multiplicar = {}
cantidadDeLetras = 0
repeticiones = 0
cantidadTotalDeLetras = 0

def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	#print "Case #"+str(case)+": "+str(texto)
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")
	
	
def getLetra(letras, posicion):
	if posicion >= cantidadTotalDeLetras: return ""
	return letras[posicion % cantidadDeLetras]

def esUltimaValor(letras, posicion):
	if (posicion % cantidadDeLetras == (cantidadDeLetras - 1)): return True
	return False
	
def resuelve(letras):
	posicionActual = 0
	letraActual = getLetra(letras, posicionActual)
	
	esUltimoValorDeCiclo = False
	ultimoValor = ""
	yaPaseUnCiclo = False
	yaPaseSegundoCiclo = False
	ultimosValoresDeCiclo = {}
	
	while(True): # Busco i
		if esUltimaValor(letras,posicionActual):
			if yaPaseUnCiclo:
				if yaPaseSegundoCiclo:
					if letraActual in ultimosValoresDeCiclo: return "NO"
					ultimosValoresDeCiclo[letraActual] = True
				else:
					yaPaseSegundoCiclo = True
			else:
				yaPaseUnCiclo = True
		if letraActual == "i":
			posicionActual += 1
			letraActual = getLetra(letras, posicionActual)
			if not letraActual: return "NO"
			break
		siguienteLetra = getLetra(letras, posicionActual+1)
		if not siguienteLetra:
			return "NO"
		letraActual = multiplicar[letraActual][siguienteLetra]
		posicionActual += 1
	
	
	yaPaseUnCiclo = False
	yaPaseSegundoCiclo = False
	ultimosValoresDeCiclo = {}
	
	while(True): # Busco j
		if esUltimaValor(letras,posicionActual):
			if yaPaseUnCiclo:
				if yaPaseSegundoCiclo:
					if letraActual in ultimosValoresDeCiclo: return "NO"
					ultimosValoresDeCiclo[letraActual] = True
				else:
					yaPaseSegundoCiclo = True
			else:
				yaPaseUnCiclo = True
		if letraActual == "j":
			posicionActual += 1
			letraActual = getLetra(letras, posicionActual)
			if not letraActual: return "NO"
			break
		siguienteLetra = getLetra(letras, posicionActual+1)
		if not siguienteLetra:
			return "NO"
		letraActual = multiplicar[letraActual][siguienteLetra]
		posicionActual += 1
	
	yaPaseUnCiclo = False
	yaPaseSegundoCiclo = False
	ultimosValoresDeCiclo = {}
	
	posicionDeK = 0
	
	while(True): # Busco k
		if esUltimaValor(letras,posicionActual):
			if yaPaseUnCiclo:
				if yaPaseSegundoCiclo:
					if letraActual in ultimosValoresDeCiclo:
						if not ("k" in ultimosValoresDeCiclo):
							# Hay un ciclo y la k no esta en el ciclo por lo
							# que no se llega a k en el final, cortamos.
							return "NO"
						else:
							if posicionDeK and letraActual == "k":
								largoDeCiclo = posicionActual - posicionDeK
								if ( (cantidadTotalDeLetras-1-posicionDeK) % largoDeCiclo) == 0:
									return "YES"
								else:
									return "NO"
							
					ultimosValoresDeCiclo[letraActual] = True
					if letraActual == "k" and posicionDeK == 0:
						posicionDeK = posicionActual
				else:
					yaPaseSegundoCiclo = True
			else:
				yaPaseUnCiclo = True
		if ( (letraActual == "k") and (posicionActual == cantidadTotalDeLetras-1) ):
			return "YES"
		siguienteLetra = getLetra(letras, posicionActual+1)
		if not siguienteLetra:
			return "NO"
		letraActual = multiplicar[letraActual][siguienteLetra]
		posicionActual += 1
		
	return
	
def lector():
	entrada = open(NOMBRE_ARCHIVO_DE_ENTRADA, 'r')

	global cantidadDeLetras
	global repeticiones
	global cantidadTotalDeLetras

	for caso in xrange(int(entrada.readline())):
		cantidadDeLetras, repeticiones = entrada.readline().split()
		
		cantidadDeLetras = int(cantidadDeLetras)
		repeticiones = int(repeticiones)
		
		cantidadTotalDeLetras = cantidadDeLetras * repeticiones
		
		letras = entrada.readline()
		
		sol = resuelve(letras)
		imprime(caso+1, sol)


def main():
	global multiplicar
	
	multiplicar["1"] = {}
	multiplicar["i"] = {}
	multiplicar["j"] = {}
	multiplicar["k"] = {}
	
	multiplicar["-1"] = {}
	multiplicar["-i"] = {}
	multiplicar["-j"] = {}
	multiplicar["-k"] = {}	
	
	# Positivos por positivos
	multiplicar["1"]["1"] = "1"
	multiplicar["1"]["i"] = "i"
	multiplicar["1"]["j"] = "j"
	multiplicar["1"]["k"] = "k"
	
	multiplicar["i"]["1"] = "i"
	multiplicar["i"]["i"] = "-1"
	multiplicar["i"]["j"] = "k"
	multiplicar["i"]["k"] = "-j"
	
	multiplicar["j"]["1"] = "j"
	multiplicar["j"]["i"] = "-k"
	multiplicar["j"]["j"] = "-1"
	multiplicar["j"]["k"] = "i"
	
	multiplicar["k"]["1"] = "k"
	multiplicar["k"]["i"] = "j"
	multiplicar["k"]["j"] = "-i"
	multiplicar["k"]["k"] = "-1"
	
	# Positivos por negativos
	multiplicar["1"]["-1"] = "-1"
	multiplicar["1"]["-i"] = "-i"
	multiplicar["1"]["-j"] = "-j"
	multiplicar["1"]["-k"] = "-k"
	
	multiplicar["i"]["-1"] = "-i"
	multiplicar["i"]["-i"] = "1"
	multiplicar["i"]["-j"] = "-k"
	multiplicar["i"]["-k"] = "j"
	
	multiplicar["j"]["-1"] = "-j"
	multiplicar["j"]["-i"] = "k"
	multiplicar["j"]["-j"] = "1"
	multiplicar["j"]["-k"] = "-i"
	
	multiplicar["k"]["-1"] = "-k"
	multiplicar["k"]["-i"] = "-j"
	multiplicar["k"]["-j"] = "i"
	multiplicar["k"]["-k"] = "1"
	
	# Negativos por positivos
	multiplicar["-1"]["1"] = "-1"
	multiplicar["-1"]["i"] = "-i"
	multiplicar["-1"]["j"] = "-j"
	multiplicar["-1"]["k"] = "-k"
	
	multiplicar["-i"]["1"] = "-i"
	multiplicar["-i"]["i"] = "1"
	multiplicar["-i"]["j"] = "-k"
	multiplicar["-i"]["k"] = "j"
	
	multiplicar["-j"]["1"] = "-j"
	multiplicar["-j"]["i"] = "k"
	multiplicar["-j"]["j"] = "1"
	multiplicar["-j"]["k"] = "-i"
	
	multiplicar["-k"]["1"] = "-k"
	multiplicar["-k"]["i"] = "-j"
	multiplicar["-k"]["j"] = "i"
	multiplicar["-k"]["k"] = "1"
	
	# Negativos por negativos
	multiplicar["-1"]["-1"] = "1"
	multiplicar["-1"]["-i"] = "i"
	multiplicar["-1"]["-j"] = "j"
	multiplicar["-1"]["-k"] = "k"
	
	multiplicar["-i"]["-1"] = "i"
	multiplicar["-i"]["-i"] = "-1"
	multiplicar["-i"]["-j"] = "k"
	multiplicar["-i"]["-k"] = "-j"
	
	multiplicar["-j"]["-1"] = "j"
	multiplicar["-j"]["-i"] = "-k"
	multiplicar["-j"]["-j"] = "-1"
	multiplicar["-j"]["-k"] = "i"
	
	multiplicar["-k"]["-1"] = "k"
	multiplicar["-k"]["-i"] = "j"
	multiplicar["-k"]["-j"] = "-i"
	multiplicar["-k"]["-k"] = "-1"
	
	lector()

salida = open(NOMBRE_ARCHIVO_DE_SALIDA, 'w')
main()
salida.close()
