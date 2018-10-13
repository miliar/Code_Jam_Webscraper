infile = 'bsmall.in'
outfile = 'bsmall.out'
import pdb
from collections import defaultdict

def main():
	with open(infile) as f, open(outfile, 'w+') as out:
		T = int(f.readline())
		for c in range(0, T):
			N, R, o, Y, G, B, V = map(int, f.readline().split(" "))
			result = stableS(N, R, Y, B)
			print(result)
			out.write('Case #{0}: {1}\n'.format(c+1, result))	
			
def stableS(n, r, y, b):
	outstring = ''
	keys = ['R', 'Y', 'B']
	values = [r, y, b]
	mosti = values.index(max(values))
	most = values.pop(mosti)
	mostl = keys.pop(mosti)
	
	if most > 0.5 * n:
		return 'IMPOSSIBLE'
	
	nmosti = values.index(max(values))
	nmost = values.pop(nmosti)
	nmostl = keys.pop(nmosti)
	
	least = values[0]
	leastl = keys[0]
	
	dif = nmost - least
	
	for i in range(0, dif):
		outstring += mostl
		most -= 1
		outstring += nmostl
		nmost -= 1
	#now nmost == least
	assert nmost == least
	
	while most >= 2: #already is 0 if nmost was equal to most. 		
		outstring += mostl
		most -= 1
		outstring += leastl
		least -= 1
		
		outstring += mostl
		most -= 1
		outstring += nmostl
		nmost -= 1
	
	if most == 1:
		outstring += mostl
		most -= 1
		outstring += leastl
		least -= 1
		outstring += nmostl
		nmost -= 1
		
	while least >= 1:
		outstring += leastl
		least -=1
		outstring += nmostl
		nmost -= 1

	assert check(outstring)
	
	return outstring

def check(string):
	for i in range(0, len(string) - 1):
		if string[i] == string[i + 1]:
			print(string)
			return False
			
	return True
		
	
				
if __name__=='__main__':
	main()
