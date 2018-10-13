file = open("Candy.txt", "r").read(100000)

filename = "out.txt"

out = open(filename, 'w')

parts = file.split("\n")
n = int(parts.pop(0))

import itertools
import copy

def calc(A):
	r = -1
	if add(A) == 0:
		r = sum(A) - min(A)
	return "NO" if r == -1 else ("%d" % r)


def add(A):
	r = 0
	for x in A:
		r = r ^ x
	return r

for i in range(1,n+1):
	N = parts.pop(0)
	A = parts.pop(0)
	out.write("Case #%d: %s\n" % (i, calc(list(map(lambda x: int(x), A.split(" "))))))

