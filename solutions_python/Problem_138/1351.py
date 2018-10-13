# -*- coding: iso-8859-1 -*-
from sys import argv
from collections import deque


def removeSmallestBiggerThen(l, x):
	i = 0;
	while l[i] < x: 
		i += 1;
	l.pop(i)	
	

def war(n, k):
	count = 0;
	for x in n : #naomi: nimmt immer das niedrigste:
		#ken: nimm das kleinste was größer ist
		if (k[-1] < x): 
			k.pop(0); #kleinstes entfernen
			count += 1;
		else:
			removeSmallestBiggerThen(k, x)
	return count

def dwar(n, k):
	count = 0;
	while len(n):
		if n[-1] > k[-1]:
			count += 1
			removeSmallestBiggerThen(n, k[0]);
			k.pop(0);
		else :
			#ken muss größten spielen, naomi kleinsten
			k.pop()
			n.pop(0)
	return count


script, filename = argv

txt = open(filename).readlines();

txt.reverse()

cases = int(txt.pop());

#print "number of test: %r" % cases

for case in range(1, cases+1):
	txt.pop(); #number of stones
	naomi = [float(i) for i in txt.pop().split()] 
	ken = [float(i) for i in txt.pop().split()] 
	naomi.sort()
	ken.sort()

	#print naomi
	#print ken	

	pwar = war(naomi, ken[:])
	pdwar = dwar(naomi,ken);
	

	print "Case #{0}: {1} {2}".format(case, pdwar, pwar)

