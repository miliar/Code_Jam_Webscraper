#!/usr/bin/env python

import sys, os
from string import whitespace
from math import pow

def main(*args):

	# Cargo los datos del problema 
	if len(sys.argv) > 1: in_f = open(sys.argv[1], 'r')
	else: in_f = open('A.in', 'r')
	in_f.readline()
	cases = [map(int, line.split(" ")) for line in in_f]	
	in_f.close()	
	
	# Creo el archivo .out
	out_f = open('A.out', 'w')
	
	# Redirecciono el standar output hacia 
	old_stdout = sys.stdout
	sys.stdout = out_f

	# Resuelvo cada caso de la entrada y guardo el resultado en el archivo
	for i in range(len(cases)):
		res = lightOn(cases[i][0], cases[i][1])
		print 'Case #' + str(i+1) + ':', 
		if res:
			print "ON"
		else:
			print "OFF"

	# Restauro el standar output original
	sys.stdout = old_stdout
	
	return 0


def lightOn(n,k):
	if(k == 0): 
		return False
	else:
		s = pow(2,n)
		return ((k%s) == (s-1))


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main(sys.argv)
