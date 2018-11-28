import sys, os

cases = int(sys.stdin.readline())

for case in xrange(cases):
    arr = sys.stdin.readline().split()
    buts = int(arr[0])
    plan = arr[1:]
    time = { 'O' : 0, 'B' : 0 }
    pos = {'O' : 1, 'B' : 1 }
    clock = 0
    for b in xrange(0,buts*2,2):
        bot = plan[b]
        tpos = int(plan[b+1])
        delta = abs(tpos-pos[bot])+1
        pos[bot] = tpos
        clock = max(clock+1,time[bot]+delta)
        time[bot] = clock
    print 'Case #%d: %d' % (case+1, clock)
        #print 'b ',b, ' bot ',bot,' tpos ', tpos, ' delta ',delta,' tbot ', time[bot], ' clock ', clock
    #print clock
        
    

    
    
    
    
