# -*- coding:utf-8 -*-
import sys

def solve(bs):
    # [(o_pos, o_t), (b_pos, b_t)]
    pos_t = [(1, 0), (1, 0)]
    t = 0
    for c, p in bs:
        dt = abs(pos_t[c][0] - p) + 1
        tmp_t = pos_t[c][1] + dt
        if tmp_t > t:
            pos_t[c] = (p, tmp_t)
            t = tmp_t
        else: # tmp_t <= t:
            t += 1
            pos_t[c] = (p, t)
    return t
            

if __name__=='__main__':
    fname = sys.argv[1]
    f = open(fname)

    t = int(f.readline().strip())
    for i in range(t):
        l = f.readline().strip().split(' ')
        n = int(l[0])
        l = l[1:]
        bs = []
        for j in range(n):
            bs.append( (0 if l[2*j]=='O' else 1, int(l[2*j+1])) ) 
        t = solve(bs)
        print "Case #%d: %d" % (i+1, t)
