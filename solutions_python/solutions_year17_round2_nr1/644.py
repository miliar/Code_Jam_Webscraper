import sys

def lastArrTime(horses, N, D):
	if(N==1) : 
		k,s = horses[0]
		return (D-k)/s

	lastTime = lastArrTime(horses[0:N-1], N-1, D)

	k,s = horses[N-1]
	myTime = (D-k)/s
	if(lastTime<myTime) : return myTime

	return lastTime




f = open('input.txt')

sys.setrecursionlimit(1500)

T = int(f.readline())

for case in range(1,T+1):
	sD,sN = f.readline(). split(" ")
	D,N=int(sD), int(sN)

	horses = [None]*N
	for i in range(0,N):
		sK, sS = f.readline(). split(" ")
		horses[i] = int(sK), int(sS)

	lastTime = lastArrTime(horses,N,D)

	print("Case #"+str(case)+": "+str(D/lastTime))
