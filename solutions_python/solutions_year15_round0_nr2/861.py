import copy

def test(p, e):
	st = 0
	p = copy.deepcopy(p)
	#import pdb; pdb.set_trace()
	while(p[0] > e-st):
		if e-st ==0:
			return False
		p.append(p[0]/2)
		p.append((p[0]+1)/2)
		p.pop(0)
		p.sort(reverse=True)
		st += 1
	return True

fr = open('in','r')
fw = open('out','w')

t = int(fr.readline().strip())
for case in range(t):
	d = int(fr.readline().strip())
	p = fr.readline().strip().split(' ')
	p = [int(num) for num in p]
	p.sort(reverse=True)
	l = 0
	r = p[0]
	while l < r:
		if test(p, (l+r)/2) == True:
			r = (l+r)/2
		else:
			l = (l+r)/2 + 1
	print "Case #%d: %d" % (case+1, r)
	fw.write("Case #%d: %d\n" % (case+1, r))
fr.close()
fw.close()
