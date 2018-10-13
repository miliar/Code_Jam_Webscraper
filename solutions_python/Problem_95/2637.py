#!/usr/bin/env python
#encoding: latin1

ent = "A-small-attempt0.in"
sal = "output.out"

entrada = open(ent, 'r')
salida = open(sal, 'w')

def imprime(case, texto):
	"""Recibe numero de case y texto que puede ser numero.
	Graba en salida."""
	salida.write("Case #"+str(case)+": "+str(texto)+"\n")

def crear_dic():
	dic = {'q': 'z','z': 'q'}
	abecedario = "abcdefghijklmnopqrstuvwxyz"
	
	lineas_code = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"]
	
	lineas_normal = ["our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"]
	
	for y in xrange(3):
		linea = lineas_code[y]
		for x in xrange(100):
			try:
				letra_code = linea[x]
				if letra_code not in dic:
					dic[letra_code] = lineas_normal[y][x]
			except IndexError:
				break
				
	return dic

def resolver(dic):
	primera_linea = True
	case = 1
	for linea in entrada:
		if primera_linea:
			primera_linea = False
			continue
		
		texto = ""
		
		for letra in linea:
			if letra == '\n': continue
			texto = texto + dic[letra]
		imprime(case, texto)
		case += 1

def main():
	dic = crear_dic()
	
	resolver(dic)
				
	
	
				
	
	
	
	
main()
entrada.close()
salida.close()
