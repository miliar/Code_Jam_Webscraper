import string
import sys

outab = "abcdefghijklmnopqrstuvwxyz"
intab = "ynficwlbkuomxsevzpdrjgthaq"

table = string.maketrans(intab, outab)

n = int(sys.stdin.readline().strip())

for i in range(n):
	l = sys.stdin.readline()
	sys.stdout.write("Case #%d: %s" % (i+1, l.translate(table))) 


