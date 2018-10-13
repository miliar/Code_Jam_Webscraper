'''
Created on 07/05/2011

@author: German
'''

_best = {}

def is_good(t_i, p, surprising):
    (q, t) = divmod(t_i, 3)
    if q>=p:
        return True
    if t>0 and q+1 >= p:
        return True
    if surprising and ((t == 2 and q +2 >= p) or \
                       (t==0) and q + 1 >= p and q-1>=0):
        return True
    return False
                       

def best(t, S, p):
    if t == []:
        return 0
    i = len(t)
    t_i = t[0]
    
    _best[(i,S)] = _best[(i-1,S)] = (1 if is_good(t_i, p, False) else 0) + best(t[1:], S, p)
    if S>0:
        _best[(i-1,S-1)] = (1 if is_good(t_i, p, True) else 0) + best(t[1:], S-1, p)
        if _best[(i-1,S-1)] > _best[(i,S)]:
            _best[(i,S)] = _best[(i-1,S-1)]
    
    return _best[(i,S)]
    

if __name__ == '__main__':
    with open('sol.out', 'w') as out:
        with open('B-small-attempt0.in', 'r') as f:
            T = int(f.readline())
            for i in xrange(1,T+1):
                case = f.readline().split()
                N = int(case.pop(0))
                S = int(case.pop(0))
                p = int(case.pop(0))
                t = []
                for j in xrange(N):
                    t.append(int(case.pop(0)))
                
                _best = {}
                res = best(t,S,p)    
                res_str = "Case #%d: %d\n" % (i, res)
                print res_str,
                out.write(res_str)