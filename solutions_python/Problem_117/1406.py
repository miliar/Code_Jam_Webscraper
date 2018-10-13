
def solve(l1,caseNum):
	n,m = map(int,l1[0].split())
	if n == 1 or m == 1:
		printRes('YES',caseNum)
		return
	lawn = [map(int,x.split()) for x in l1[1:]]

	for i in range(n):
		for j in range(m):
			if not check(i,j,lawn, n, m):
				printRes('NO',caseNum)
				return

	printRes('YES',caseNum)
	
def check(i,j,lawn,n,m):
	vb = False
	hb = False
	x = [x for x in lawn[i] if x > lawn[i][j]]
	if x:
		vb = True

	y = [x[j] for x in lawn if x[j] > lawn[i][j]]
	if y:
		hb = True


	if vb and hb:
		return False
	return True

def printRes(a,caseNum):
	o.write('Case #'+ str(caseNum) + ': ' + a + '\n')
	print 'Case #'+ str(caseNum) + ': ' + a

f = open('input.in', 'r')
o = open('out.txt','w')
lines = f.read().splitlines()
cases = int(lines[0])
cl = 1
for i in range(1,cases+1):
	le = int(lines[cl].split()[0])
	solve(lines[cl:cl+le+1],i)
	cl += le + 1

f.close()
o.close()