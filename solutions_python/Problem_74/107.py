def parse(s):
    return [s[2*i] for i in xrange(len(s)/2)],map(int,[s[2*i+1] for i in xrange(len(s)/2)])

def next(lst,i,val):
    try:
        return lst.index(val,i)
    except:
        return None

def sign(x):
    if x>0: return 1
    elif x<0: return -1
    else: return 0

def advance(steps,cur,target):
    if target is None:
        return cur
    elif abs(cur-but[target])<=steps:
        return but[target]
    else:
        return cur+steps*sign(but[target]-cur)
        
other={'O':'B','B':'O'}
for case in range(input()):
    bot,but=parse(raw_input().split()[1:])
    #print bot,but
    pos={'O':1,'B':1}
    time=0
    for i in xrange(len(bot)):
        target={'O':next(bot,i,'O'),'B':next(bot,i,'B')}
        curbot=bot[i]
        otherbot=other[curbot]
        timediff=abs(but[i]-pos[curbot])+1
        pos[curbot]=but[i]
        time+=timediff
        pos[otherbot]=advance(timediff,pos[otherbot],target[otherbot])
        #print pos,time,target,time,timediff
    print "Case #"+str(case+1)+":",
    print time
