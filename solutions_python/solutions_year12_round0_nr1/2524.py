import sys
import string

	#print "Case #",i+1,":", str.translate(table)
intab = "ynficwlbkuomxsevzpdrjgthaq"
outta = "abcdefghijklmnopqrstuvwxyz"

table = string.maketrans( intab , outta )


f = open("A-small-attempt1.in", "r")
n = f.readline()
n = int(n)
for i in range(n):
	str = f.readline()
	str = str.rstrip()
	print 'Case #%(Case)d: %(stuff)s' % {"Case" : i+1, "stuff" : str.translate(table)}