#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():

	t = int(raw_input())

	for j in xrange(1, t + 1):
	
		N_int = raw_input()

		doitContinuer = True
		while doitContinuer:
			list_chiffres_N = []
			N_int = int(N_int)
			N_str_original = str(N_int)
			list_chiffres_N = [i for i in N_str_original]
			list_chiffres_N = map(int, list_chiffres_N)
			list_chiffres_N_sorted = sorted(list_chiffres_N)
			if list_chiffres_N_sorted == list_chiffres_N:
				print "Case #{}: {}".format(j, N_int)
				doitContinuer = False
			else:
				N_int -= 1
				doitContinuer = True

if __name__ == '__main__':
	main()
