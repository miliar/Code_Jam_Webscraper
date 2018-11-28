def p2(N,R,O,Y,G,B,V):
	liste = [[R,'R'],[B,'B'],[Y,'Y']]
	liste.sort(reverse=True)
	
	res = ""
	
	prev = ''
	
	for i in range(N):
		if prev == liste[0][1]:
			if liste[1][0] <= 0:
				return 'IMPOSSIBLE'
			prev = liste[1][1]
			liste[1][0] -= 1
		else:
			prev = liste[0][1]
			liste[0][0] -= 1
		res += prev
		liste.sort(reverse=True)
		
	if N!=1 and prev == res[0]:
		err = res[0]
		res = res[:-1]
		for i in range(N-2):
			if res[i] != err and res[i+1] != err:
				res = res[:i+1] + err + res[i+1:]
				break
		if len(res) != N:
			return 'IMPOSSIBLE'
	return res
		
	
	
	
T = int(input())
for t in range(T):
	N, R, O, Y, G, B, V = list(map(int,input().split()))
	print("Case #%d: %s"%(t+1,p2(N,R,O,Y,G,B,V)))
