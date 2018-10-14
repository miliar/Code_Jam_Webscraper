from heapq import heappush,heappop,heapify
fr=open('C-small-2-attempt2.in','r')
fw=open('out_ppp4.txt','w')
T=int(fr.readline())
for z in range(T):
	N,K=fr.readline().split(' ')
	#print N,K
	N,K=int(N),int(K)
	q=[-N]
	print z
	if K>N*3/5:
		fw.write('Case #%d: %d %d\n'%(z+1,0,0))
		continue
	for j in range(K):
		t=-heappop(q)
		a,b=(t-1)/2,(t-1-(t-1)/2)
		heappush(q,-a)
		heappush(q,-b)
		if j==K-1: fw.write('Case #%d: %d %d\n'%(z+1,max(a,b),min(a,b)))
	#fw.write('Case #%d: %s\n'%(z+1,ans))
