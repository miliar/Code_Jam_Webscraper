import scanf

d = {'a':'y', 'o':'e', 'z':'q', ' ':' ', 'q':'z'}

fi = file("qa.in")
fo = file("qa.out")

try:
	while 1:
		d.update(zip(scanf.readstr(fi), scanf.readstr(fo)))
except EOFError:
	pass
	
from sys import stdin
n = scanf.readint(stdin)
for i in xrange(1,n+1):
	print "Case #%d:"%i, ''.join(map(lambda c:d[c], scanf.readline(stdin)))
