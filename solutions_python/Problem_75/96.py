import sys

cin = sys.stdin.readline


def solve(combins, destroys, s):
    lis = []
    for c in s:
        lis.append(c)
        if len(lis) < 2:
            #print lis
            continue
        a, b = lis[-1], lis[-2]
        if (a,b) in combins:
            lis.pop()
            lis.pop()
            lis.append(combins[(a,b)])
        elif (b,a) in combins:
            lis.pop()
            lis.pop()
            lis.append(combins[(b,a)])

        #destroy check
        se = set(lis)
        if any(i[0] in se and i[1] in se for i in destroys):
            lis = []
        #print lis
    return '[' + ', '.join(lis) + ']'
            
        

if __name__ == '__main__':
    T = int(cin())
    for cn in xrange(T):
        lin = cin().strip().split()
        lin.reverse()
        C = int(lin.pop())
        cc = [lin.pop() for i in xrange(C)]
        D = int(lin.pop())
        dd = [lin.pop() for i in xrange(D)]
        N = lin.pop()
        s = lin.pop()
        combin = dict(((i[0], i[1]), i[2]) for i in cc)
        destroys = set((i[0], i[1]) for i in dd)
        print "Case #{0}: {1}".format(cn+1, solve(combin, destroys, s))
                    
            
        
    
