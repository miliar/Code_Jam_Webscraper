T = input()
from string import maketrans
table = maketrans('ynficwlbkuomxsevzpdrjgthaq','abcdefghijklmnopqrstuvwxyz')
n=1;
while n <= T:
	Text = raw_input()
	text = Text.translate(table)
	print "Case #%d:" %n + " %s" %text
	n = n+1

