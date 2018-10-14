'''
Created on May 4, 2013

@author: santosh
'''

if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(T):
        (mote, t1) = [int(i) for i in raw_input().split()]
        all_motes = sorted([int(i) for i in raw_input().split()])
        sp = 0
        s = [0 for i in xrange(len(all_motes))]
        if mote == 1:
            sp = len(all_motes)
        else :
            cur_mote = mote
            for i in xrange(len(all_motes)):
                    while cur_mote <= all_motes[i]:
                        cur_mote = cur_mote + cur_mote - 1
                        s[i]+=1
                    cur_mote += all_motes[i]
            sp=sum(s)
            if sp>0:
                sp=min(sp,min([sum(s[:i])+len(s[i:]) for i in xrange(len(s))]))           
                
        print 'Case #%d: %d' % (t + 1,sp)
