import sys, os

def flip(string, start, l):
	for i in xrange(start, start+l):
		if string[i]=='-':
			string[i]='+'
		else:
			string[i]='-'

def flips(string, k):
	
	index = 0
	flips = 0
	
	while index < len(string)-k+1:

		if string[index]=='-':
			flips += 1
			flip(string, index, k)

		index += 1

	return (-1 if '-' in string else flips) 


def main():
	T = int(raw_input())

	for t in xrange(T):
		line = raw_input().split()
		result = flips(list(line[0]), int(line[1]))
		pr = 'IMPOSSIBLE' if result<0 else str(result)
		print 'Case #'+str(t+1)+': '+pr


main()