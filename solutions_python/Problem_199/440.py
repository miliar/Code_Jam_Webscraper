debug = True
_print = print
def print(*args, d=True, end='\n'):
	e = end
	if(debug or not d):
		_print(*args, end=e)
		
def printTc(t_c):
	print("Case #%d: " % (t_c+1), end="")

t = int(input())

for t_c in range(t):
	pstr, k = input().split()
	k = int(k)
	size = len(pstr)
	pstr = [a == "+" for a in pstr]

	i = 0
	flips = 0
	while i <= size-k:
		if not pstr[i]:
			flips += 1
			for j in range(i, i+k):
				pstr[j] = not pstr[j]
		i += 1
	
	printTc(t_c)
	ok = True
	for x in range(size-k, size):
		if not pstr[x]:
			print("IMPOSSIBLE", d=False)
			ok = False
			break
	if ok:
		print(flips, d=False)