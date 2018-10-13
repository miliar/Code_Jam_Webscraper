"""Code written using Python 2.7.5, http://www.python.org/"""

import string

def calcDeceit(naomi, ken):
	points = 0
	while len(naomi) > 0:
		n = naomi.pop(0)
		if n > ken[0]:
			ken.pop(0)
			points += 1
		else:
			ken.pop()

	return points


def calcWar(naomi, ken):
	points = 0

	while len(naomi) > 0:
		n = naomi.pop()
		if n > ken[-1]:
			points += 1
			ken.pop(0)
		else:
			for k in ken:
				if k > n:
					ken.remove(k)
					break


	return points

def calc(case):
	naomi = sorted([float(e) for e in case[1].split()])
	ken = sorted([float(e) for e in case[2].split()])

	dw = calcDeceit(naomi[:], ken[:])
	w = calcWar(naomi, ken)
	
	return ("%(dw)i %(w)i" % {'dw':dw, 'w':w})

	
		
		
def main():
	f = open('D-large.in', 'r')
	lines = f.readlines()
	f.close()
	c = int(lines[0].split()[0])
	#print c
	cases = [r.strip() for r in lines[1:]]
	#print cases

	of = open('output_d_large.txt', 'w')

	for idx in range(0, c):
		of.write('Case #%(idx)i: %(i)s\n' % {'idx': idx + 1, 'i': calc(cases[idx*3:idx*3 + 3])})

	of.close()

main()
#import timeit
#print timeit.timeit("main()", setup="from __main__ import main", number=1)
