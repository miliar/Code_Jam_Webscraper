#!/usr/bin/env python

import sys, os
from string import whitespace
from math import pow

def main(*args):

	# Cargo los datos del problema 
	if len(sys.argv) > 1: in_f = open(sys.argv[1], 'r')
	else: in_f = open('_C.in', 'r')
	nbr_cases = int(in_f.readline())
	cases = [map(int, line.split(" ")) for line in in_f]	
	in_f.close()	
	
	# Creo el archivo .out
	out_f = open('C.out', 'w')
	
	# Redirecciono el standar output hacia out_f
	old_stdout = sys.stdout
	sys.stdout = out_f

	# Resuelvo cada caso de la entrada y guardo el resultado en el archivo
	j = 0
	for i in range(nbr_cases):
		roller_coaster = cases[j]
		queue = cases[j+1]
		print 'Case #' + str(i+1) + ':', dayProfit(roller_coaster, queue)
		j += 2
	
	# Restauro el standar output original
	sys.stdout = old_stdout
	
	return 0


def dayProfit(rc, q):
	runs, profit = rc[0], 0
	while runs > 0:
		free_seats, in_game = rc[1], []
		while free_seats > 0 and len(q) > 0:
			next_group = q.pop(0)
			if next_group > free_seats:
				q.insert(0, next_group)
				break
			else:
				in_game.append(next_group)
				free_seats -= next_group
				profit += next_group
		q.extend(in_game)
		runs -= 1
			
	return profit


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main(sys.argv)
