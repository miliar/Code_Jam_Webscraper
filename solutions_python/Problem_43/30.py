import sys, re
readline = sys.stdin.readline

def gen_values():
    yield 1
    yield 0
    v=2
    while True:
        yield v
        v+=1

N = int(readline())
for case in range(1, 1 + N):
    num = readline().strip()
    values = gen_values()
    digs={}
    for d in num:
        if d not in digs:
            digs[d]=values.next()
    base = max(digs.values())+1
    tot=0
    for d in num:
        tot=tot*base+digs[d]
    print "Case #%s: %s"%(case,tot)
    
    
    
        
    
