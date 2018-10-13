def solve(crypted):
    map={}
    base=max(2, len(set(crypted)))
    candidates=range(base-1, -1, -1)
    if len(candidates)>0:
        candidates[-1]=1
    if len(candidates)>1:
        candidates[-2]=0
    sum=0
    for c in crypted:
        if not (c in map):
            n=candidates.pop()
            map[c]=n
        else:
            n=map[c]
        sum=sum*base+n
    return sum


import sys
f=sys.stdin
next(f)

for i, crypted in enumerate(f):
    print 'Case #%d: %d' % (i+1, solve(crypted.strip()))


