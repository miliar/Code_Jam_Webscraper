
def step(me, other, order):
	posm, turnm = me
	poso, turno = other
	return (order, max(abs(posm-order)+turnm+1, turno+1))

def solve(pb):
	n=pb[0]
	O=(1,0)
	B=(1,0)
	for i in xrange(int(n)):
		if pb[i*2+1] == 'O':
			O=step(O,B,int(pb[i*2+2]))
		else:
			B=step(B,O,int(pb[i*2+2]))
	posO, turnO = O
	posB, turnB = B
	return max(turnO, turnB)

if __name__ == '__main__':
	n = int(raw_input())
	b = [[_ for _ in raw_input().split()] for i in xrange(n)]
	for i in xrange(n):
		print 'Case #'+str(i+1)+': '+str(solve(b[i]))
    

