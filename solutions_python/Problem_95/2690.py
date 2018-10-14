#!/usr/bin/env python
from string import maketrans

def convert(sInput):
	intab = "abcdefghijklmnopqrstuvwxyz"
	outtab= "yhesocvxduiglbkrztnwjpfmaq"
	transtab = maketrans(intab, outtab)
	return sInput.translate(transtab)

def main():
	iNumCases = input()
	lCases = []
	for i in xrange(0,iNumCases):
		sStr = raw_input()
		lCases.append(str(sStr))
	c = 1
	for sCase in lCases:
		print 'Case #{0}: {1}'.format(c, convert(sCase))
		c += 1

if __name__ == '__main__':
	exit(main())
