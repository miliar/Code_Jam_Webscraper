'''
Created on 2011-5-7

@author: LJY
'''
import psyco

psyco.full()
def work(p , pos, lastcost):
    cost = 0
    if p[0] != pos:
        cost += abs(pos - p[0])
        p[0] = pos
    p[1] += cost + 1
    if p[1] <= lastcost:
        p[1] = lastcost + 1
    return p
print 'starting'
fin=file('a.in')
fout=file('a.out','w')
T=int(fin.readline().strip())
for t in range(T):

    line = fin.readline().strip().split()[1:];
    po = [1,0]
    pb = [1,0]
    for l in range(len(line)/2):
        pos = int(line[l*2+ 1])
        key = line[l*2]
        if key == 'O':
            po = work(po, pos, pb[1])
        else:
            pb = work(pb, pos, po[1])
    rst = max(po[1],pb[1])
    fout.write("Case #%d: %d\n" % (t+1, rst)) 
fout.close()
print 'ok'
