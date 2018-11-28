#!/usr/bin/python
#This program requires python ver 2.6 or higher. (itertools.combinations)
import sys
import itertools

#double
def df(x):
	return x * 2

#booster
def booster(way, num):
	current = 0
	sortway = way[:]
	sortway.sort(reverse=True)
	for target in sortway[:num]:
		way[current + way[current:].index(target)] /= 2

#solve case function
def solve_case(L, t, way, case_number):
	spent = 0
	is_boosted = False
	while len(way) > 0:
		d = way.pop(0)
		if t - d < 0 and not is_boosted:
			xd = d - t 
			spent += t
			way.insert(0, xd)
			booster(way, L)
			is_boosted = True
		else:
			spent += d
			t -= d

	print "Case #" + str(case_number) + ": " + str(spent)

#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	line = r.readline().strip().split(' ')
	L = int(line[0])
	t = int(line[1])
	N = int(line[2])
	a = line[4:]
	way = []
	for x in range(0, N):
		way.append(int(a[x % len(a)]))
	dway = map(df, way)
	solve_case(L, t, dway, case_number)

