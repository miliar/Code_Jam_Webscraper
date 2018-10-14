import re,sys
def _scans():
	while True:
		yield from input().split()
scans = _scans().__next__
scan = lambda: int(scans())
red = lambda *a,**kw:print(*a,**kw,file=sys.stderr)

def recur(n,r,y,b,last,first):
	for i in 'RYB':
		if i==last:
			continue
		if n==1:
			if i==first:
				continue
			if i=='R':
				if r<=0:
					continue
			if i=='Y':
				if y<=0:
					continue
			if i=='B':
				if b<=0:
					continue
			return i
		if i=='R':
			if r<=0:
				continue
			ret = recur(n-1,r-1,y,b,i,first if first else i)
			if ret:
				return i + ret
		if i=='Y':
			if y<=0:
				continue
			ret = recur(n-1,r,y-1,b,i,first if first else i)
			if ret:
				return i + ret
		if i=='B':
			if b<=0:
				continue
			ret = recur(n-1,r,y,b-1,i,first if first else i)
			if ret:
				return i + ret


def inter(A,B):
	out = ''
	for i,j in zip(A,B):
		out += i+j
	return out


def calc_inner(r,y,b):
	n=r+y+b
	dom = max(r,y,b)
	if n-dom < dom:
		return 'IMPOSSIBLE'
	if n-dom == dom:
		if r==dom:
			return inter('R'*dom,'B'*b+'Y'*y)
		if b==dom:
			return inter('B'*dom,'R'*r+'Y'*y)
		if y==dom:
			return inter('Y'*dom,'B'*b+'R'*r)
	t=n-dom-dom
	if t==dom:
		return 'RYB'*t
	ret = calc_inner(r-t,y-t,b-t)
	if ret[0] == 'R':
		return 'RBY'*t+ret
	if ret[0] == 'Y':
		return 'YRB'*t+ret
	if ret[0] == 'B':
		return 'BYR'*t+ret

def calc(n,r,o,y,g,b,v):
	# o <> b
	# g <> r
	# v <> y
	if o+b == n and o==b:
		return 'OB'*o
	if g+r == n and g==r:
		return 'GR'*r
	if v+y == n and v==y:
		return 'YV'*v
	b -= o
	if o>0 and b < 1:
		return 'IMPOSSIBLE'
	r -= g
	if g>0 and r < 1:
		return 'IMPOSSIBLE'
	y -= v
	if v>0 and y < 1:
		return 'IMPOSSIBLE'
	ret = calc_inner(r,y,b)
	if ret == 'IMPOSSIBLE':
		return ret
	return (ret.
		replace('B','B'+'OB'*o,1).
		replace('R','R'+'GR'*g,1).
		replace('Y','Y'+'VY'*v,1))

# import random
# for _ in range(100):
# 	r,y,b = random.randrange(100),random.randrange(100),random.randrange(100)
# 	a = recur(r+y+b,r,y,b,'','')
# 	z = calc(r+y+b,r,0,y,0,b,0)
# 	if (not a) ^ (z == 'IMPOSSIBLE'):
# 		print(a,z,r,y,b)


'''
if True:
	'''
sys.stdin = open('input.txt')
with open('output.txt','w') as sys.stdout:#'''
	for t in range(scan()):
		red('Case #%d'%(t+1))
		print('Case #%d: %s'%(t+1,calc(*[scan() for i in range(7)])))