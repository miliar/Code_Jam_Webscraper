import fileinput

words = []
for line in fileinput.input():
	for word in line.split():
		words.append(word.strip())
def nextInt():
	return int(words.pop(0))
def nextStr():
	return words.pop(0)


def go(a):
	n = len(a)
	has = 0
	friends = 0
	for i in range(n):
		needed = i
		if needed > has:
			friends += needed - has
			has += needed - has
		has += a[i] 
	return friends

def main():
	T = nextInt()
	for i in range(T):
		smax = nextInt()
		x = nextStr()
		a = []
		for j in range(0,smax+1):
			a.append(int(x[j]))
		print "Case #%d: %d"%(i+1, go(a))
			 






main()