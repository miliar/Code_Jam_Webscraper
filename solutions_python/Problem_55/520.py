import math

#
#Input

#3
#4 6 4		Case #1: 21
#1 4 2 1	Case #2: 100
#100 10 1	Case #3: 20

#1
#5 5 10
#2 4 2 3 4 2 1 2 1 3

def ThemePark(R,k,q,G):
	"""
		R = quantidade de voltas
		k = tamanho do carrinho
		q = total de grupos
		G = grupos
	"""
	G = [int(j) for j in G.split(" ")]
	euros = 0
	offset = 0
	while R:
		c = 0
		for x in G:
			x = G[offset]			
			c += x
			if c > k:
				c -= x
				break
			offset = (offset +1) % len(G)
		euros += c
		R -= 1
	return euros

def testCase(fname):
	fin = open('%s.in' % fname, 'r')
	fout = open('%s.out' % fname, 'w')
	
	inread = fin.readlines()
	fin.close()
	
	count = int(inread[0])
	x = 1
	y = 1
	while count:
		print x
		R,k,q = inread[x].split(" ")
		G = inread[x+1]
		fout.write('Case #%d: %s\n' % (y, ThemePark(int(R),int(k),int(q),G)) )
		x += 2
		y += 1
		count -= 1

testCase('C-small-attempt1')