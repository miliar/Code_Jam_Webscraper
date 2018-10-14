#!/usr/bin/env python
import sys

def read(fn):
	T=0
	n=0
	header = True
	for i,l in enumerate(file(fn)):
		l=l.strip()
		if i==0: 
			T=int(l)
			maps = [0]*T
			continue
		l = map(int, l.split())
		if header:
			H,W = l
			header = False
			maps[n] = (H,W,[])
			continue
		else:
			if H>1:
				maps[n][2].append(l)
				H-=1
			else:
				maps[n][2].append(l)
				H-=1
				n+=1
				header = True
	return maps

def solve(m):
	alphabet  = map(chr, range(ord('a'),ord('z')+1))
	alphabet2 = map(chr, range(ord('A'),ord('Z')+1))
	H,W,map_ = m
	res = []
	for i in range(H):
		res.append(['-'] * W)

	def neighbors(m,i,j):
		res = []
		if i>0:   res.append(m[i-1][j])
		else  :   res.append(99999)

		if j>0:   res.append(m[i][j-1])
		else  :   res.append(99999)

		if j<W-1: res.append(m[i][j+1])
		else  :   res.append(99999)

		if i<H-1: res.append(m[i+1][j])
		else  :   res.append(99999)

		return res

	s = 0
	for i in range(H):
		for j in range(W):
			sink = True
			n = neighbors(map_,i,j)
			for x in n:
				if map_[i][j] > x: 
					sink = False
					break
			if sink:
				#res[i][j] = alphabet[s] # TODO: teh wrong
				#res[i][j] = alphabet2[s]
				res[i][j] = 'S'
				s+=1

	for i in range(H):
		for j in range(W):
			if res[i][j]!='-': continue
			n = neighbors(map_,i,j)
			res[i][j] = str(n.index(min(n)))

	def next(res,i,j):
		if res[i][j]=='0': return i-1, j
		if res[i][j]=='1': return i  , j-1
		if res[i][j]=='2': return i  , j+1
		if res[i][j]=='3': return i+1, j
		print i,j

	s = 0
	#print res
	for i in range(H):
		for j in range(W):
			if res[i][j] in ['0','1','2','3','S']: 
				tomark = []
				ni,nj=i,j
				while res[ni][nj] in ['0','1','2','3']:
					tomark.append( (ni,nj) )
					ni,nj = next(res, ni, nj)

				tomark.append( (ni,nj) )
				#print tomark
				flag = False
				for ii, jj in tomark:
					#res[ii][jj] = res[ni][nj]
					if res[ni][nj] == 'S':
						res[ii][jj] = alphabet[s]
						flag = True
					else:
						res[ii][jj] = res[ni][nj]

				if flag: s += 1

	return res

def main(argv):
	maps = read(argv[1])
	#print maps
	for i,m in enumerate(maps):
		res = solve(m)
		print "Case #%d:" % (i+1)
		for row in res:
			print " ".join(row)

if __name__ == "__main__":
	main(sys.argv)
