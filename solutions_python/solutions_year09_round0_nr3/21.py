#!/usr/bin/python
import sys
import psyco
psyco.full()
rdl = sys.stdin.readline

MEMO = {}
def eat(s, food):
    if (s, food) in MEMO: return MEMO[(s, food)]
    l = s[0]
    next = s[1:] if len(s) > 1 else None
    if next == None: 
        return food.count(l)
    if len(food) == 0 or l not in food: return 0
    cur = food
    count = 0
    while l in cur:
        count += eat(next, cur[cur.index(l)+1:]) +\
                 eat(s, cur[cur.index(l)+1:])
        break
    #print repr(s),'sta',count,'volte in',repr(food)
    MEMO[(s, food)] = count
    return count
              
        
    

def process(case):
    """precessing case #"""
    #[int(x) for x in sys.stdin.readline().split()]
    wcj = 'welcome to code jam'
    sub = ''.join([i for i in rdl() if i in wcj])
    cur = sub
    return str(eat(wcj, cur)%10000).zfill(4)
        
        

   

    return str(count%10000).zfill(4)



cases = int(rdl())
for case in xrange(1, cases+1):
    print "Case #%d:"%case, process(case)
