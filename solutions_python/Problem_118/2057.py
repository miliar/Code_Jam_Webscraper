import math

def readFile(filename):
	f = file(filename)
	count = int(f.readline())
	print count
	contents = f.readlines()[:count]
	return [s.split() for s in contents]

def judge(number):
	if number==1: return True
	s = str(number)
	sr = s[::-1]
	print s, sr
	sqr = math.sqrt(number)
	if s==sr and int(sqr)==sqr and p(int(sqr)):
		return True
	return False
def p(number):
	s = str(number)
	sr = s[::-1]
	return sr==s

if __name__ == '__main__':
	cs = readFile('C-small-attempt0.in.txt')
	o = file('r.txt', 'w')
	# print cs
	for j,a in enumerate(cs[0:]):
		count = 0
		l = int(a[0])
		b = int(a[1])
		for x in xrange(l,b+1):
			if (judge(x)):
				count += 1
				print x
		o.write('Case #'+str(j+1)+': '+str(count)+'\n');

	print math.sqrt(676)