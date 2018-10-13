
import sys

numo = 0;
IN = sys.stdin

def line(typ=int):
	i = IN.readline().strip()
	return typ(i)
	
def split(typ=int):
	return [typ(x) for x in IN.readline().split()]
	
	
def case():
	global numo
	numo	+= 1
	return 'Case #%d:' % numo

def run():
	t = line()
	
	for _ in xrange(t):
		line()
		li = sorted(split())
		l = li[0]
		r = reduce(lambda x,y: x^y, li[1:])
		c = sum(li[1:])
		i =1
		while(l != r and i < len(li)):
			l ^= li[i]
			r ^= li[i]
			c -= li[i]
			i +=1
		print case(),
		if ( i == len(li)):
			print 'NO'
		else:
			print c
	
run()