#!/usr/bin/env python
import sys

def main():
	f = sys.stdin

	n = int(f.readline().strip())
	for i in range(n):
		p, k, l = [int(x) for x in f.readline().strip().split(" ")]
		rawf = [int(x) for x in f.readline().strip().split(" ")]
		freq = []
		for j in range(l):
			freq.append((j, rawf.pop(0)))

		freq.sort(key=lambda x: x[1], reverse=True)
		total = 0
		impossible = False

		key = 0
		for j, fr in freq:
			total += (key / k + 1) * fr
			if key / k + 1 > p:
				impossible = True
				break
			key+= 1

		answer = str(total)
		if impossible:
			answer = "Impossible"

		print "Case #%i: %s" % (i + 1, answer)

if __name__ == "__main__":
	main()
