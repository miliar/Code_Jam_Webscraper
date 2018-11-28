#!/usr/bin/env python

import sys
from collections import deque
import random,datetime,multiprocessing

def calc_profit_slow(case,runs,coaster_size,group_count,groups,debug =False):
    sys.stderr.write('%s %s %s %s\n' % (runs,coaster_size,group_count,','.join([repr(x) for x in groups])))
    q=deque(groups[:])
    total = 0
    for run in xrange(runs):
        acc = 0
        riders = []
        while len(q) > 0:
            group = q.popleft()
            if (acc + group) <= coaster_size:
                acc += group
                riders.append(group)
            else:
                q.appendleft(group)
                break
                
        total += acc
        q.extend(riders)
        
    return (case,total)

def calc_profit_fast(case,runs,coaster_size,group_count,groups,debug=False):
    if debug:
        sys.stderr.write('%s %s %s\n' % (runs,coaster_size,group_count))
    start = datetime.datetime.now()
    c=0

    q_idx = 0
    total = 0

    for run in xrange(runs):
        if debug and c == 0:
            now = datetime.datetime.now()
            delta = now - start
            ms = delta.microseconds
            start = now
            c=100000
            sys.stderr.write('[%s] %s us/run\n' % (run, float(ms)/c))
        c = c-1
        acc = 0
        while True:
            new = acc+groups[q_idx]
            if new <= coaster_size:
                next = q_idx +1

                if next >= group_count:
                    q_idx = 0
                else:
                    q_idx = next

                acc = new
            else:
                break

        total += acc

    return (case,total)

def calc_profit_faster(case,runs,coaster_size,group_count,groups,debug=False):
    if debug:
        sys.stderr.write('%s %s %s\n' % (runs,coaster_size,group_count))
    start = datetime.datetime.now()
    c=0

    q_idx = 0
    total = 0

    max_groups = group_count
    
    factor = runs
    if factor > 1000:
        factor = 1000
    
    group_count = group_count * factor
    groups = groups * factor

    for run in xrange(runs):
        if debug and c == 0:
            now = datetime.datetime.now()
            delta = now - start
            ms = delta.microseconds
            start = now
            c=100000
            sys.stderr.write('[%s] %s us/run\n' % (run, float(ms)/c))
        c = c-1
        acc = 0
        num_groups = 0
        while True:
            new = acc+groups[q_idx]
            new_num_groups = 1 + num_groups
            if new <= coaster_size and new_num_groups <= max_groups:
                next = q_idx +1
                
                if next >= group_count:
                    q_idx = 0
                else:
                    q_idx = next
                    
                acc = new
                num_groups = new_num_groups

            else:
                break

        total += acc

    return (case,total)

func = calc_profit_fast

def mfunc(args):
    return func(*args)
    
if __name__ == '__main__':
    debug = False
    src = ''
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'slow':
            func = calc_profit_slow
        elif sys.argv[1] == 'faster':
            func = calc_profit_faster
        elif sys.argv[1] == 'test':
            debug = True
            src = '''\
4
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
1000 100 10
4 3 9 1 2 5 6 9 1 10

'''
        elif sys.argv[1] == 'bigtest':
            debug = True
            src = '''\
1
100000000 1000000000 1000
'''
            groups = []
            for n in xrange(1000):
                groups.append(str(random.randint(1,10000000)))
            src += ' '.join(groups)
            src += '\n'
#            print src
            if len(sys.argv) > 2:
                if sys.argv[2] == 'faster':
                    func = calc_profit_faster
    if not src:
        src = sys.stdin.read()
        
    lines = src.split('\n')
    runs = int(lines[0])
    cases = []
    
    for run in xrange(0,runs):
        R,k,N = [int(x) for x in lines[(run*2)+1].split(' ')]
        groups = [int(x) for x in lines[(run*2)+2].split(' ')]
        assert int(N) == len(groups)
        cases.append([run+1,int(R),int(k),int(N),groups,debug])
            
    pool = multiprocessing.Pool()
    
    output = pool.map(mfunc,cases)
    pool.close()
    pool.join()
    
    output.sort()
    
    for out in output:
        print "Case #%s: %s" % out
    
    # for case in cases:
    #     print "Case #%s: %s" % func(*case)
         