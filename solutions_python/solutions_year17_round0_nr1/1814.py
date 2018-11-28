# Google Code Jam 2016
# Qualification Round
# Problem A. Oversized Pancake Flipper

import sys

def flip(p, start, k):
    f = ''
    for i in range(k):
        if p[start+i] == '-':
            f += '+'
        else:
            f += '-'        
    return p[0:start] + f + p[start+k:]
   

def oversized_pancake_flipper_iter(s, v, k, n, debug=False):
    if debug:
        print n+1, s,v
        
    q = s    
    t = set()
    
    n +=1
    
    while len(q) > 0:
        e = q.pop()
        
        for i in range(len(e) - k + 1):
            flipped_e = flip(e,i,k)
            
            if debug:
                if flipped_e in v:
                    print "    " + flipped_e + " *"
                else:
                    print "    " + flipped_e
            
            if flipped_e.find('-') == -1:
                return n
                
            if flipped_e not in v:
                v.add(flipped_e)
                t.add(flipped_e)
                
    if len(t) == 0:
        return 'IMPOSSIBLE'
                
    return oversized_pancake_flipper_iter(t, v, k, n, debug)
    
    
def oversized_pancake_flipper(p, k):
    if p.find('-') == -1:
        return 0
        
    return oversized_pancake_flipper_iter(set({p}), set({p}), k, 0)
    

def solver():
    # t: the number of cases
    t = int(raw_input())
    
    for i in xrange(1, t+1):
        p, k = raw_input().split(' ')

        k = int(k)

        ans = oversized_pancake_flipper(p, k)
        
        print "Case #{}: {}".format(i, ans)


def main():
    sys.setrecursionlimit(10000)
    solver()

if __name__ == '__main__':
    main()