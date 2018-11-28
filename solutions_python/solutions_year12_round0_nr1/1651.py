#!/usr/bin/python
import string
import sys

mapping = string.maketrans("acbedgfihkjmlonqpsrutwvyxz", "yehosvcdxiulgkbzrntjwfpamq")

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1][:-2] + 'out', 'w')


	for case in xrange(1, int(infile.readline())+1):
		inline = infile.readline()

		outfile.write("Case #%i: %s"%(case, string.translate(inline, mapping)))

if __name__ == "__main__":
		main()
