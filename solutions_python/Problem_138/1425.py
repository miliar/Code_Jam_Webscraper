def solveDeWar():
	counter = 0
	pos1 = 0
	pos2 = 0
	for i in range(N):
		if(n[pos1] > k[pos2]):
			counter+=1
			pos1+=1
			pos2+=1
		else:
			if(n[pos1] < k[pos2]):
				pos1+=1 

	return counter


def solveWar():
	counter = 0
	pos1 = 0
	pos2 = 0
	for i in range(N):
		if(n[pos1] > k[pos2]):
			counter+=1
			pos2+=1
		else:
			if(n[pos1] < k[pos2]):
				pos1+=1 
				pos2+=1

	return counter

def main():
	T = input()
	for x in range(T):
		global n, k, N
		N = input()
		n = map(float, raw_input().split())
		k = map(float, raw_input().split())
		k.sort()
		n.sort()
		print "Case #"+ str(x+1) + ": "+ str(solveDeWar()) + " " + str(solveWar())

main();