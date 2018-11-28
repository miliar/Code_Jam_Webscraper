debug = True
_print = print
def print(*args, d=True, end='\n'):
	e = end
	if(debug or not d):
		_print(*args, end=e)

def printTc(t_c):
	print("Case #%d: " % (t_c+1), d=False, end="")

t = int(input())
for t_c in range(t):
	n = [int(x) for x in input()]
	size = len(n)
	
	i = 0
	last = n[0]
	while i < size:
		if n[i] < last:
			last = n[i]
			break
		last = n[i]
		i += 1
	if i < size:
		i -= 1
		while i > 0:
			if n[i]-1 >= n[i-1]:
				break
			i -= 1
		n[i] -= 1
		for j in range(i+1, size):
			n[j] = 9
	printTc(t_c)
	leadZ = True
	for k in n:
		if k != 0:
			leadZ = False
		if not leadZ:
			print(k, end="", d=False)
	print(d=False)