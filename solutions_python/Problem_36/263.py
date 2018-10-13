import re
import sys

if __name__ == '__main__':
	in_filename = "C-small.in"
	#in_filename = "C-dummy.in"
	#in_filename = "C-large.in"
	out_filename = "C-small.out"
	#out_filename = "C-large.out"
	
	in_file = open(in_filename, 'r')
	out_file = open(out_filename, 'w')

	num_cases = int(in_file.readline())
	for case in range(0,num_cases):
		text = in_file.readline()
		sen = "welcome to code jam"
		W = len(text)
		H = len(sen)
		tab = [0]*W*H
		for r in range(0,H):
			sum = 0
			for c in range(0,W):
				cursor = r*W + c
				if r == 0 and text[c] == sen[0]:
					tab[cursor] = 1
				else:
					sum = (sum + tab[(r-1)*W + c]) % 10000
					if text[c] == sen[r]:
						tab[cursor] = sum
			#print tab[r*W:r*W+W]

		# Sum last row
		answer = reduce(lambda x,y: x + y, tab[(H-1)*W:H*W])
		out_file.write("Case #%d: %04d\n" % ((case+1), answer))
		#print '-'*80
	out_file.close()

