from heapq import *

fi = open("C-small-1-attempt0.in")
fo = open("C-small-1-attempt0.out", "w")

line = next(fi)
T = int(line)
for t in range(T):
	line = next(fi)
	[N,K] = [int(x) for x in line.rstrip().split(' ')]
	stalls = []
	heappush(stalls, [N-(N-1)//2,N-N//2,(N-1)//2,(N-1)//2,N//2])
	for i in range(1,K):
		prev = heappop(stalls)
		if prev[3]>0:
			heappush(stalls, [N-(prev[3]-1)//2,N-prev[3]//2,prev[2]-prev[3]//2-1,(prev[3]-1)//2,prev[3]//2])
		if prev[4]>0:
			heappush(stalls, [N-(prev[4]-1)//2,N-prev[4]//2,prev[2]+(prev[4]-1)//2+1,(prev[4]-1)//2,prev[4]//2])

	last = heappop(stalls)
	fo.write("Case #" + str(t+1) + ": " + str(N-last[1]) + " " + str(N-last[0]) + "\n")

fi.close()
fo.close()
