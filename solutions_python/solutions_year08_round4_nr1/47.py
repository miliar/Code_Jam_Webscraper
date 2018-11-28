import sys

readline = sys.stdin.readline
def readstrlist():
	return readline().split()

def readintlist():
	return map (int,readstrlist())

LARGE=1000000
#n[0]=out,[1]=op,[2]=chang

def minchang (want, root, nod):
	if want == nod[root][0]:
		return 0
	
	if nod[root][2]:		#chang?
		if nod[root*2][0] != nod[root*2+1][0]:
			return 1
		
		
		if nod[root][1]:		#AND
			if want:
				return 1+min(minchang (1,root*2, nod),minchang(1,root*2+1,nod))
			else:
				return min (minchang (0,root*2, nod),minchang(0,root*2+1,nod))
		else:					#OR
			if want:
				return min (minchang (1,root*2, nod),minchang(1,root*2+1,nod))
			else:
				return 1+min (minchang (0,root*2, nod),minchang(0,root*2+1,nod))
			
	if nod[root][1]==None:
		return LARGE
	
	if nod[root][1]:		#AND
		if want:
			return minchang (1,root*2, nod)+minchang(1,root*2+1,nod)
		else:
			return min (minchang (0,root*2, nod),minchang(0,root*2+1,nod))
	else:					#OR
		if want:
			return min (minchang (1,root*2, nod),minchang(1,root*2+1,nod))
		else:
			return minchang (0,root*2, nod)+minchang(0,root*2+1,nod)
	

if __name__ == "__main__":
	for i in range(1, int(readline())+1):
		
		(M,V) =  readintlist ()
		nod=[False]
		intnods = (M-1)/2
		for j in range(1,M+1):
			if j <= intnods:
				(G,C)=readintlist()
				nod.append([None,G,C])
				#print j, nod
			else:
				nod.append([int(readline()),None,None])
				#print j, nod
		#print nod,intnods
		for j in range (intnods,0,-1):
			if nod[j][1]:
				nod[j][0] = nod[j*2][0] and nod[j*2+1][0]
			else:
				nod[j][0] = nod[j*2][0] or nod[j*2+1][0]
		#print V, nod
		
		sol = minchang (V,1,nod)
		if sol >= LARGE:
			print "Case #%d: IMPOSSIBLE" % i
		else:
			print "Case #%d: %d" % (i, sol)