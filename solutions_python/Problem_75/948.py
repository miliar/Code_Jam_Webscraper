#!/usr/bin/python

import sys
import re

def main():
	if len(sys.argv) < 3:
		print "Needs input and output files"
		sys.exit(1)

	fin = open(sys.argv[1], 'r')
	fout = open(sys.argv[2], 'w')

	cases = int(fin.readline())

	for c in range(cases):
		combine = []
		opposed = []

		s = fin.readline().strip().split(r' ')

		for i in range(int(s.pop(0))):
			chars = list(s.pop(0))
			combine.append(re.compile(chars[0] + chars[1] + '|' + chars[1] + chars[0]))
			combine.append(chars[2])

		for i in range(int(s.pop(0))):
			chars = list(s.pop(0))
			opposed.append(re.compile(chars[0] + r'.*' + chars[1] + '|' + chars[1] + r'.*' + chars[0]))

		length = int(s.pop(0))
		magic = s.pop(0)
			
		elements = list(magic)
		invoked = ''

		for e in elements:
			invoked += e
			
			for p in range(len(combine) / 2):
				invoked = combine[2 * p].sub(combine[2 * p + 1], invoked)
	
			for p in opposed:
				if p.search(invoked):
					invoked = ''
					break

		fout.write("Case #%d: [" % (c + 1))
		for i in range(len(invoked)):
			if i > 0:
				fout.write(", ")
			fout.write(invoked[i])
		fout.write("]\n")
			
	fin.close()
	fout.close()

if __name__ == '__main__':
	main()
