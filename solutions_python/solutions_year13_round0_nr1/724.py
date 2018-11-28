import sys
T = int(sys.stdin.readline())

def checkWinner(l):
	for p in ['X', 'O']:
		if l.count(p)==4: return p
		if l.count(p)==3 and 'T' in l: return p
	return None

for t in range(T):
	G = [[],[],[],[]]
	status = None
	for i in range(4):
		G[i]= sys.stdin.readline().strip()
	sys.stdin.readline()
	winner = checkWinner([G[i][i] for i in range(4)])
	if winner:
		print("Case #%s: %s won" % (str(t+1), winner))
		continue
	winner = checkWinner([G[i][3-i] for i in range(4)])
	if winner:
		print("Case #%s: %s won" % (str(t+1), winner))
		continue
	next=False
	for i in range(4):
		winner = checkWinner(G[i])
		if winner:
			print("Case #%s: %s won" % (str(t+1), winner))
			next=True
			break
	if next: continue
	for i in range(4):
		winner = checkWinner([G[j][i] for j in range(4)])
		if winner:
			print("Case #%s: %s won" % (str(t+1), winner))
			next=True
			break
	if next: continue
	empty = False
	for i in range(4):
		if '.' in G[i]:
			print("Case #%s: Game has not completed" % (str(t+1)))
			empty = True
			break
	if not empty:
		print("Case #%s: Draw" % (str(t+1)))
