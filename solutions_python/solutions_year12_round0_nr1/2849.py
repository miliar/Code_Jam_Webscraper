#!/usr/bin/python -tt

from sys import stdin
from string import rstrip

def main():
	lines = stdin.readlines()
	g2e = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
	result = []

	def translate(line):
		result = []
		for c in rstrip(line):
			result += g2e[c]

		return ''.join(result)

	for i in xrange(1, len(lines[1:]) + 1):
		print 'Case #' + str(i) + ':', translate(lines[i])

	return

if __name__ == '__main__':
	main()