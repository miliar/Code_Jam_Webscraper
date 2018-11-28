#!/usr/bin/python

fileNameBase = 'A-large'

def gcd_impl(a, b):
	while b != 0:
		a, b = b, a%b
	return a

def gcd(a, b):
	if a > b: return gcd_impl(a, b)
	elif b > a: return gcd_impl(b, a)
	else: return a

def solve(line):
	N, Pd, Pg = (int(n) for n in line.split())
	Dc = gcd(Pd, 100)
	Dnum = Pd/Dc
	Dden = 100/Dc
	#Gc = gcd(Pg, 100)
	#Gnum = Pg/Gc
	#Gden = 100/Gc
	if Dden > N: return 'Broken'
	#D = Dnum
	if Pg == 100 and Pd != 100: return 'Broken'
	if Pg == 0 and Pd != 0: return 'Broken'
	return 'Possible'

fin = file(fileNameBase+'.in')
fout = file(fileNameBase+'.out', 'w')
N = int(fin.readline().strip())
for i in xrange(N):
	line = fin.readline().strip()
	res = solve(line)
	fout.write('Case #')
	fout.write(str(i+1))
	fout.write(': ')
	fout.write(str(res))
	fout.write('\n')
fin.close()
fout.close()

