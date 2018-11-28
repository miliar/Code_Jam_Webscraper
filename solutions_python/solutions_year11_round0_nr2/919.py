#!/usr/bin/python
# -*- coding: utf-8 -*-
## Problem B. Magicka (GCJ Qualif 2011)


def magick(tab):
	c = int(tab[0])
	comb = [] ## combinaison : [cara1, cara2, [fusion]]
	for k in tab[1:c+1]:
		comb.append(k[:-1])
		comb.append([k[-1]])
	
	d = int(tab[c+1])
	oppo = [] ## suppression : [chaine]
	for k in tab[c+2:d+1+c+1]:
		oppo.extend(list(k))
	
	n = int(tab[d+1+c+1])
	ent = tab[-1] ## entree

	## Parse !
	sol = [ent[0]]
	
	for k in xrange(1, n):
		k_sol = len(sol) ## indice pour sol
		a = ent[k]
		
		if k_sol == 0:
			sol.append(a)
		else:
			b = sol[k_sol-1] + a ## cara-1 + cara
			## comb
			if b in comb:
				ind = comb.index(b) + 1
				sol[k_sol-1] = comb[ind][0]
			## comb
			elif b[::-1] in comb:
				ind = comb.index(b[::-1]) + 1
				sol[k_sol-1] = comb[ind][0]
			## opp
			elif a in oppo:
				del_sol = 0 ## memoire, pas de suppr => append
				for i_op, op in enumerate(oppo):
					if op == a: ## a in oppo
						if i_op % 2 == 0: # i_op est pair
							epsilon = 1
						else: ## i_op impair
							epsilon = -1
						op_plus = oppo[i_op + epsilon] ## the opposite
						if op_plus in sol[:k_sol]:
							sol = []
							del_sol = 1
							break
				if del_sol == 0:
					sol.append(a)
			else:
				sol.append(a)
	
	return "[" + ", ".join(_ for _ in sol) + "]"


if __name__ == "__main__":
	T = int(raw_input())
	for k in xrange(T):
		tab = raw_input().split()
		char = "Case #%d: %s" %(k+1, magick(tab))
		print char