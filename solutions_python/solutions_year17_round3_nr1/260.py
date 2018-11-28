t=int(input())
import numpy as np
for i in range(1,t+1):
	N,K=[int (s) for s in input().split(" ")]
	pancakelist=np.zeros((N,2))
	for j in range(0,N):
		Ri,Hi=[int (s) for s in input().split(" ")]
		pancakelist[j][0]=2*np.pi*Ri*Hi#side
		pancakelist[j][1]=np.pi*Ri**2#top
	#print(pancakelist)
	#print("p")
	argsort=pancakelist[:,0].argsort()
	pancakelistsort=np.sort(pancakelist,axis=0)
	pancakelistsort=pancakelist[argsort]
	#print(pancakelistsort.shape)
	#sortbytop=np.sort(pancakelistsort[0:2][K:])
	#print(sortbytop)
	#p=pancakelistsort[(N-K):][1]
	maxtop=np.max(pancakelistsort[(N-K):,1])
	toreplace=maxtop+pancakelistsort[N-K][0]
	for j in range(0,N-K):
		if pancakelistsort[j][0]+pancakelistsort[j][1]>toreplace:
			toreplace=pancakelistsort[j][0]+pancakelistsort[j][1]
	if K>1:
		print("Case #{}: {}".format(i,toreplace+np.sum(pancakelistsort[(N-K+1):,0])))
	else:
		print("Case #{}: {}".format(i,toreplace))
	#print(pancakelistsort)
	#print(maxtop)
	#print(toreplace)