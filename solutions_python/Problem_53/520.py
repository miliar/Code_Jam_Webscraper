#!/usr/bin/env python
import sys,math
import multiprocessing

def mfunc(args):
    return snapper_faster(*args)
    
def snapper_slow(run,snappers,snaps):
    snappers = [0,] * snappers
    print "Case: %s" % run
    for snap in xrange(snaps):
        print snappers,
        on = True
        for snapper in snappers:
            if snapper == 0:
                on = False
                break
        print on
        last = 1
        for snapper in xrange(len(snappers)):
            if last:
                if snappers[snapper] == 1:
                    last = 1
                    snappers[snapper] = 0
                else:
                    snappers[snapper] = 1
                    last = 0
                    break
        
        
    on = True
    for snapper in snappers:
        if snapper == 0:
            on = False
            break
                

    print snappers,
    print on
    
    return (run,'ON' if on else 'OFF')

def snapper_fast(run,snappers,snaps):
    all_on = math.pow(2,snappers)
    on = ((snaps+1) % all_on) == 0
    return (run,'ON' if on else 'OFF')

def snapper_faster(run,snappers,snaps):
    all_on = int(math.pow(2,snappers))
    on = (snaps & (all_on-1)) == (all_on-1)
    return (run,'ON' if on else 'OFF')
    

if __name__ == '__main__':
    debug = False
    src = ''
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            debug = True
            src = '''\
9
1 0
1 1
4 0
4 47
2 0
2 1
2 2
2 3
2 4
'''

    if not src:
        src = sys.stdin.read()
        
    lines = src.split('\n')
    runs = int(lines[0])
    cases = []
    
    for run in xrange(0,runs):
        N,K = [int(x) for x in lines[run+1].split(' ')]
        cases.append([run+1,int(N),int(K)])
            
    pool = multiprocessing.Pool()
    
    output = map(mfunc,cases)
    pool.close()
    pool.join()
    
    output.sort()
    
    for out in output:
        print "Case #%s: %s" % out
