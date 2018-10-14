T = int(raw_input())
for i in range(T):
    j = int(raw_input())
    for k in range(4):
        a = raw_input()
        if k==j-1:
            s = map(int,a.split())
    j=int(raw_input())
    for k in range(4):
        a = raw_input()
        if k==j-1:
            t = map(int,a.split())
    r = set(s)
    r = r.intersection(t)
    if len(r)==1:
        r=str(list(r)[0])
    elif len(r)==0:
        r="Volunteer cheated!"
    else:
        r="Bad magician!"
    print 'Case #'+str(i+1)+': '+r
