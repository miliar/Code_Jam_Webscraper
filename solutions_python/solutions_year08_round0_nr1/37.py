

class A(object):
    def __init__(self):
        self.S = int(raw_input())
        self.names = {}
        for i in xrange(self.S):
            name = raw_input()
            assert name not in self.names
            self.names[name] = len(self.names)
        
        self.pos = {}
        for s in xrange(self.S):
            self.pos[s] = []
        
        self.Q = int(raw_input())
        self.query = []
        for i in xrange(self.Q):
            name = raw_input()
            s = self.names[name]
            self.query.append(s)
            self.pos[s].append(i)
            
        
        
        
    def go(self):
        if not self.Q: return 0
        curr = -1
        sw   = -1
        for i,q in enumerate(self.query):
            if curr != -1 and q != curr: continue
            
            max = -1
            cho = -1
            for s in xrange(self.S):
                if s == curr:   continue
                p = self.pos[s]
                while p and p[0] < i: p.pop(0)
                if not p or p[0] > max:
                    max = not p and self.Q+1 or p[0]
                    cho = s
                
                
            assert cho != -1
            assert cho != q
            assert cho != curr
            
            curr = cho
            sw += 1
        
        return sw



if __name__ == '__main__':
    
    N = int(raw_input())
    for i in xrange(N):
        a = A()
        print 'Case #%d: %d' % (i+1, a.go())
        