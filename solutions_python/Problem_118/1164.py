import bisect
import sys

maxr = 0
fslist = []

def nonzeroes():
	for d in range(1, 10):
		yield str(d)

def digits():
	for d in range(10):
		yield str(d)

def palin_prefixes(n):
	def prefixes(n):
		if n > 1:
			for d in digits():
				for p in prefixes(n-1):
					yield d + p
		else:
			for d in digits():
				yield d
	if n > 1:
		for first in nonzeroes():
			for p in prefixes(n-1):
				yield first + p
	elif n == 1:
		for first in nonzeroes():
			yield first
	else:
		yield ""

def is_palin(n):
	return str(n)[::-1] == str(n)
		
def __init__(length):
	def insertif(p):
		t = int(p) ** 2
		if is_palin(t):
			fslist.append(t)
	for l in range(1, length+1):
		if l % 2 == 1:
			for prefix in palin_prefixes(l/2):
				for d in nonzeroes():
					palin = prefix + d + prefix[::-1]
					insertif(palin)
		else:
			for prefix in palin_prefixes(l/2):
				palin = prefix + prefix[::-1]
				insertif(palin)
		print "Done", l, len(fslist), fslist

def fs(L, R):
	return bisect.bisect_right(fslist, R) - bisect.bisect_left(fslist, L)

def __main__():
	with open(sys.argv[1], "r") if len(sys.argv)==2 else sys.stdin as input:
		T = int(input.readline())
		inputlist = [map(int, input.readline().split()) for _ in range(T)]
		anslist = map(fs, *zip(*inputlist))
	with open(sys.argv[1]+".out", "w") if len(sys.argv)==2 else sys.stdin as output:
		for i, ans in enumerate(anslist, start=1):
			output.write("Case #{}: {}\n".format(i, ans))

__init__(8)
if __name__ == "__main__":
	__main__()