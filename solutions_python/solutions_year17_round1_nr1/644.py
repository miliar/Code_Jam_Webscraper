import sys
import math
f = open('out17Q1a.out','w')
T = int( sys.stdin.readline().strip())
case =0
sys.setrecursionlimit(10000000)

# G ={}

# G[1]= [0,0]
def ExpandY(G,y, em,R):
	CheckRouteY(G,y-1,y,em,R)
	CheckRouteY(G,y+1,y,em,R)
def Expand(G,x,L):
	CheckRoute(G,x-1,L)
	CheckRoute(G,x+1,L)
def CheckRoute(G,x,L):
	if (x < 0 or x >= len(G)  ):
		return False
	# print(len(G),x)
	if(G[x]=='?'):
		G[x] = L
		CheckRoute(G,x-1,L)
		CheckRoute(G,x+1,L)
	return False

def CheckRouteY(G,y,L,em,R):
	if (y < 0 or y >= R  ):
		return False
	# print(len(G),y)
	if(y in em):
		# print("COPIAS")
		em.pop(y)
		G[y] = G[L]
		CheckRouteY(G,y-1,L, em,R)
		CheckRouteY(G,y+1,L,em,R)
	return False

while( T>0 ):
	T-=1
	case+=1
	R,C=    [int(s) for s in    sys.stdin.readline().strip().split() ]
	mtx = [[]*C for i in range(R)]
	empties={}
	for r in range(R):
		mtx[r]=list(  sys.stdin.readline().strip() )
		# if case == 12:
		# 	print(mtx[r])
		someLetter = False
		for c in range(C):
			if mtx[r][c] != '?':
				Expand(mtx[r],c,mtx[r][c])
				someLetter |= True
		if  not someLetter:
			empties[r] =1
	for r in range(R):
		if r not in empties:
			ExpandY(mtx,r, empties,R)
			# print(mtx[r][c])

	resp= [R,0]
	stack ={}
	stack[R] =1

	if case == 44:
		for l in mtx:
			print (''.join(l))
	# print(  " obtuve ", resp)
	# print ("Case #"+str(case)+": "+"")
	f.write ("Case #"+str(case)+": "+"\n")
	for l in mtx:
		# print (''.join(l))
		f.write (''.join(l))
		f.write ("\n")
	# break
f.close();
