#!/usr/bin/env python

import sys
count = int(sys.stdin.readline())

for i in range(count):
    data = sys.stdin.readline().split()
    o = {'p':1, 'g':0, 'c':0}
    b = {'p':1, 'g':0, 'c':0}
    c = 1
    actionsa = []
    actionsb = []
    sequence = []
    for j in range(int(data[0])):
        if data[c] == 'O':
            o['g'] = int(data[c+1])
            steps = o['g'] - o['p']
            sign = 1
            if steps < 0:
                steps = steps * -1
                sign = -1
            for k in range(steps):
                actionsa.append(1 * sign)
                o['p'] += 1 * sign
            actionsa.append('P')
            sequence.append(('O', o['g']))

        elif data[c] == 'B':
            b['g'] = int(data[c+1])
            steps = b['g'] - b['p']
            sign = 1
            if steps < 0:
                steps = steps * -1
                sign = -1
            for k in range(steps):
                actionsb.append(1 * sign)
                b['p'] += 1 * sign
            actionsb.append('P')
            sequence.append(('B', b['g']))
        c = c + 2        
    

    state = {'O':{'p':1, 'g':0, 'c':0}, 'B': {'p':1, 'g':0, 'c':0}}
    t = 0
    while (len(sequence) > 0):
        #print "\ntime: %s" % t
        #print state
        #print sequence
        #print actionsa
        #print actionsb
        t+=1
        om = 0
        bm = 0
        if len(actionsa) != 0:
            if actionsa[0] != 'P':
                state['O']['p'] += actionsa[0]
                actionsa = actionsa[1:]
                om = 1
        
        if len(actionsb) != 0:
            if actionsb[0] != 'P':
                state['B']['p'] += actionsb[0]
                actionsb = actionsb[1:]
                bm = 1
            
        
        if sequence[0][0] == 'O':
            if om == 0 and state['O']['p'] == sequence[0][1]:
                actionsa = actionsa[1:]
                sequence = sequence[1:]
        elif sequence[0][0] == 'B':
            if bm == 0 and state['B']['p'] == sequence[0][1]:
                actionsb = actionsb[1:]
                sequence = sequence[1:]

    print "Case #%i: %i" % (i+1, t)
