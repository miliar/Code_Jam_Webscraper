#!/usr/bin/python

import sys

def handle_case(K,B,T,x,v):
	arr = []
	for chick in zip(x,v):
		arr.append([chick, float(B-chick[0])/chick[1]])
	arr = sorted(arr, key=lambda x: x[1])
	count = 0
	for el in arr:
		if el[1] <= T:
			count += 1
		else:
			break
	if count < K:
		return "IMPOSSIBLE"
	last = []
	for el1 in arr[:count]:
		counter = 0
		x1,v1 = el1[0]
		for el2 in arr[count:]:
			x2,v2 = el2[0]
			if v1!=v2:
				cross = float(x1-x2)/float(v2-v1)
				if cross >=0 and cross <= T:
					counter += 1
		last.append(counter)
	last.sort()
	return str(sum(last[:K]))

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		(N,K,B,T) = map(int,fsock.readline().rstrip("\n").split(" "))
		x = map(int,fsock.readline().rstrip("\n").split(" "))
		v = map(int,fsock.readline().rstrip("\n").split(" "))
		print "Case #%d: %s" % (case, handle_case(K,B,T,x,v))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

