import csv

def magicTrick(infile):
    reader = csv.reader(open(infile,'r'),delimiter=' ')
    t,t0 = int(reader.next()[0]),0
    while t0 < t:
	wanted,w2 = set(),set()
	t0 += 1
	n = int(reader.next()[0])
	k = 4
	while k > 0:
	    k -= 1
	    n -=1
	    row = reader.next()
	    if n == 0:
		for num in row:
		    wanted.add(int(num))

	n = int(reader.next()[0])
	k = 4
	while k > 0:
	    k -= 1
	    n -=1
	    row = reader.next()
	    if n == 0:
		for num in row:
		    w2.add(int(num))
	res = wanted & w2
	if len(res) == 1:
	    rstr = res.pop()
	elif len(res) == 0:
	    rstr = 'Volunteer cheated!'
	else:
	    rstr = 'Bad magician!'
	print 'Case #%s: %s' % (t0,rstr)

if __name__ == '__main__':
    magicTrick('magicTrick.small')
