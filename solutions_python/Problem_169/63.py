class Valve:
	def __init__(self, r, c):
		self.r = r
		self.c = c
	def __lt__(self, rhs):
		return self.r < rhs.r
def solve():
        line = raw_input()
        N, V, X = line.split()
        N = int(N)
        V = float(V)
        X = float(X)
        Vs = []
        Cs = []
        for i in xrange(N):
                r, c = map(float, raw_input().split())
                v = Valve(r, c)
                Vs.append(v)
                Cs.append(c)
        if X > max(Cs) or X < min(Cs):
                return 'IMPOSSIBLE'
        if N == 1:
                return V / Vs[0].r
        X = X * V
        Vs = sorted(Vs)[::-1]
        r1 = Vs[0].r
        r2 = Vs[1].r
        c1 = Vs[0].c
        c2 = Vs[1].c
        if c1 == c2:
                return '%.7f' % (V/(r1+r2))
        t1 = (X-c2*V)/((c1-c2)*r1)
        t2 = (V-r1*t1)/r2
        return "%.7f" % max(t1, t2)
		
		
	
	

T = int(raw_input())
for i in xrange(T):
	print 'Case #%d: %s' % (i+1, solve())

