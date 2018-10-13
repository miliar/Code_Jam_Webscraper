
import sys
from StringIO import StringIO

def translate():
	example = """ejp mysljylc kd kxveddknmc re jsicpdrysizq
our language is impossible to understandqz
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities
de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up"""
	e = StringIO(example)
	d = {}
	for i in range(3):
		 l0 = list(e.readline())
		 l1 = list(e.readline())
		 d.update({x:y for x, y in zip(l0, l1)})

	del d['\n']
	return d

def solve(d):
	l = sys.stdin.readline().strip()
	return "".join(d[s] for s in list(l))

def Main():
	test = int(sys.stdin.readline())
	d = translate()
	for i in range(1, test+1):
		result = solve(d)
		print 'Case #{}: {}'.format(i, result)

if __name__ == '__main__':
	Main()