import sys,operator
sys.stdin = open('stdin.txt','r')
sys.stdout = open('stdout.txt','w')
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
t=int(input())
for u in range(t):
	n,k=map(int,input().split())
	l=[]
	for i in range(n):
		temp=list(map(float,input().split()))
		l.append(temp)
	l.sort(reverse=True)
	for i in range(n):
		l[i][1] = 2*3.14159265359*l[i][0]*l[i][1]
	m=0.0
	for i in range(n-k+1):
		_l = l[i+1:n]
		#print(_l)
		tot = l[i][1]+l[i][0]*l[i][0]*3.14159265359
		_l.sort(key=operator.itemgetter(1),reverse=True)
		for j in range(k-1):
			tot+=_l[j][1]
		#print(tot)
		if(tot>m):
			m=tot
	print("Case #"+str(u+1)+": "+str(m))



