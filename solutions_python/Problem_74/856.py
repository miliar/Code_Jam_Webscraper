#!/usr/bin/env python

def read_data(inp):
    D = inp.split("\n")[1:]
    R = []
    for r in D:
        R.append([])
        row = r.split()[1:]
        for k in range(0,len(row),2):
            a = row[k], int(row[k+1])
            R[-1].append(a)
    return R

def run_case(d):
    #print d
    if not d:
        return
    ticks = 0
    cursor = 0
    pos = {'O':1,'B':1}
    next = {'O':0,'B':0}
    for check in 'O','B':
        for a in d:
            if a[0]==check:
                next[check] = a[1]
                break
    while cursor < len(d):
        ticks += 1
        typ,where = d[cursor]
        
        for check in 'O','B':
            if typ == check:
                if pos[check] == where:
                    cursor += 1
                    #print "click",check
                    for a in d[cursor:]:
                        if a[0]==check:
                            next[check] = a[1]
                            break
                elif pos[check] > where:
                    pos[check] -= 1
                else:
                    pos[check] += 1
            else:
                if pos[check] > next[check] :
                    pos[check] -= 1
                elif pos[check] < next[check] :
                    pos[check] += 1
        #print ticks, cursor, pos, next
    return ticks
            
        
def process_data(D):
    k = 1
    for d in D:
        t = run_case(d)
        if t:
            print "Case #%d: %d" %(k,t)
        k += 1
inp = open("c:\\downloads\\A-large.in").read()

D = read_data(inp)

process_data(D)


