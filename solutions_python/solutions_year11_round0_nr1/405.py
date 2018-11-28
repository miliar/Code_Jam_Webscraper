from collections import defaultdict
from collections import deque

f=open("input.txt")
cases=int(f.readline())
def other_rb(rb):
    return ('B' if rb=='O' else 'O')

for i in xrange(0,cases):
    n=f.readline().rstrip().split(" ")
    ctr=0
    sqc = int(n[ctr])
    steps=0
    seq=[]
    o=[];
    b=[];
    rb_pos={'O':1,'B':1}
    rb_act={'O':deque([]),'B':deque([])}
    for j in xrange(0,sqc):
        ctr+=1
        r = n[ctr]
        ctr+=1
        p = int(n[ctr])
        seq.append((r,p,))
        rb_act[r].append(p)
    for s in seq:
        rb=s[0]
        orb=other_rb(rb)
        rbm=s[1]
        if len(rb_act[orb]) > 0: # there are other moves
            move_other = True
        else:
            move_other = False
        while rb_pos[rb] != rbm:
            if rb_pos[rb] < rbm: rb_pos[rb]+=1
            if rb_pos[rb] > rbm: rb_pos[rb]-=1
            if move_other:
                if rb_pos[orb] < rb_act[orb][0]: rb_pos[orb] += 1
                if rb_pos[orb] > rb_act[orb][0]: rb_pos[orb] -= 1
            steps += 1
        if move_other:
                if rb_pos[orb] < rb_act[orb][0]: rb_pos[orb] += 1
                if rb_pos[orb] > rb_act[orb][0]: rb_pos[orb] -= 1
        steps += 1 # press the button
        rb_act[rb].popleft()
    print "Case #%d: %d"%(i+1, steps)
f.close()