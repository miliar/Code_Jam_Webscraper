N = int(raw_input())
def solve(tab):
	wyn = 0;
	cycles = []
	checked = [False]*len(tab)
	for i in range(len(tab)):
		j = i
		current = 0
		while(not checked[j]):
			checked[j] = True
			j = tab[j]-1
			current+=1
		cycles.append(current)
	
	for x in cycles:
		if(x>=2):
			wyn+=x
	print float(wyn)
			
for t in range(N):
	m = raw_input()
	T = [int(x) for x in raw_input().split()]
	print "Case #"+str(t+1)+":",
	solve(T)
