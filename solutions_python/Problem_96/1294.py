y = False
b = 1
for l in open('B-large.in', 'r'):
    if not y:
        y = True
        continue
    S, p = l.strip().split(' ')[1:3]
    S, p = int(S), int(p)
    r = 0
    for i in l.strip().split(' ')[3:]:
        i = int(i)
        if i < p: continue
        elif i < (3*p-4): continue
        elif i == (3*p-4) or i == (3*p-3):
            if S!=0:
                S-=1
                r+=1
        else: r+=1
    print "Case #%d:" % b, r
    b+=1