import sys

fin = sys.stdin
fout = sys.stdout

d = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

T = int(fin.readline().strip())

for c in range(T):
	fout.write("Case #%d: " % (c+1,))
	line = fin.readline().strip()
	a = ""
	for x in line:
		if x.isalpha():
			a += d[x]
		else:
			a += x
	fout.write(a)
	fout.write("\n")