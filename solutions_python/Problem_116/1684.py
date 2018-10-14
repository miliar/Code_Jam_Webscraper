def format(l):
	row = l
	col = ["".join(x) for x in zip(*l)]
	a, b = "",""
	for x in range(4):
		a += l[x][x]
		b += l[x][3-x]
	dia = [a,b]
	return (row, col, dia)

def checkWin(l, n):
	notC = False
	for i in l:
		for j in i:
			if '.' in j:
				notC = True
			t = j.count('T')
			if j.count('X')+t == 4:
				print "Case #%d: X won" % n
				return
			if j.count('O')+t == 4:
				print "Case #%d: O won" % n
				return
	print (notC and ("Case #%d: Game has not completed" %n)
			or ("Case #%d: Draw" %n))

def main():
	nl = int(raw_input())
	inp = []
	for i in range(nl):
		whole = []
		for j in range(4):
			whole.append(raw_input().strip())
		inp.append(whole)
		try:
			raw_input()
		except:
			pass
	for i in range(nl):
		checkWin(format(inp[i]), i+1)

main()