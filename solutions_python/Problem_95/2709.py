import sys
import string

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

try:
	counter = 0
	for line in fin.readlines():
		if counter > 0:
			dst = line.translate(string.maketrans('ynficwlbkuomxsevzpdrjgthaq', 'abcdefghijklmnopqrstuvwxyz'))
			dst = 'Case #' + str(counter) + ': ' + dst
			fout.write(dst)
		counter = counter + 1
finally:
	fin.close()
	fout.close()
