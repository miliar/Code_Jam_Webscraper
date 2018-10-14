from sys import *

f = open('A-large.in', 'r')
o = open('aout', 'w')

def solve(_, sm, sa):
	count = 0
	for i in range(sm+1):
		s = int(sa[i])
		if(s == 0):
			while(s == 0):
				i += 1
				s = int(sa[i])
			sums = 0
			for j in range(i):
				sums += int(sa[j])
			if((sums + count) < i):
				diff = i - (sums + count)
				count += diff;
	o.write("Case #%d: %d\n" %(_+1, count))
			 

cases = int(f.readline())
for _ in range(cases):
	sm, sa = list(map(str,f.readline().split()))
	sm = int(sm)
	solve(_, sm, sa)
