import sys
rl = sys.stdin.readline

n = int(rl().strip())

ot = [i for i in range(0,11) ] # one to ten
for i in range(n):
    tkn = rl().strip().split()
    nn = int(tkn[0])
    ns = int(tkn[1])
    p = int(tkn[2])
    numSuprise = 0
    numGreater = 0
    for j in range(3, len(tkn)):
        num = int(tkn[j])
        isSuprise=False
        greaterThan=False
        sample = set()
        for a in ot:
            for b in ot:
                if abs(a-b) > 2: continue
                for c in ot:
                    if abs(a-c) > 2: continue
                    if abs(b-c) > 2: continue
                    if a+b+c == num:
                        if abs(a-c)==2 or abs(a-b) == 2 or abs(b-c) == 2:
                            isSuprise=True
                        if a>=p or b>=p or c>=p:
                            greaterThan=True
                        sample.add( (isSuprise, greaterThan) )
                        isSuprise, greaterThan = False, False
        if (False, True) in sample :
            numGreater += 1
        elif (True, True) in sample:
            numSuprise += 1
    ans = numGreater
    ans = ans + min(numSuprise, ns)
    print 'Case #%d: %d' % (i+1, ans) 

