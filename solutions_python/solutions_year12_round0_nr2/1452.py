#!/usr/bin/python
import sys

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1][:-2] + 'out', 'w')

	for case in xrange(1, int(infile.readline())+1):
		inp = [int(i) for i in infile.readline().split()]

		googlers = inp[0]
		surprising = inp[1]
		p = inp[2]
		points = sorted(inp[3:], reverse=True)
		result = 0
		for i in xrange(googlers):
			score1 = points[i]/3
			score2 = score1
			remainder = points[i] % 3
			score1 += remainder>0
			score2 += remainder==2

			if score1 == p-1 and surprising and score1 == score2 and score2>0:
				surprising -= 1
				score1+=1

			if score1 >= p:
				result+=1

		outfile.write("Case #%i: %i\n"%(case, result))

if __name__ == "__main__":
	main()
