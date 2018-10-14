'''
Created on May 4, 2013

@author: santosh
'''

if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(T):
        (mote, t1) = [int(i) for i in raw_input().split()]
        all_motes = sorted([int(i) for i in raw_input().split()])
        
        sums = [0 for i in xrange(len(all_motes))]
        
        stps = 0
        if mote == 1:
            stps = len(all_motes)
        else :
            cur_mote = mote
            for i in xrange(len(all_motes)):
                    while cur_mote <= all_motes[i]:
                        cur_mote = cur_mote + cur_mote - 1
                        sums[i]+=1
                    cur_mote += all_motes[i]
            stps=sum(sums)
            if stps>0:
                stps=min(stps,min([sum(sums[:i])+len(sums[i:]) for i in xrange(len(sums))]))           
                
        print 'Case #%d: %d' % (t + 1,stps)
