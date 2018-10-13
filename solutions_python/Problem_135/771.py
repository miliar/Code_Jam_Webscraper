t = input()
for i in range(t):
    a = []
    b = []
    m = input()
    for i in range(4):
        dummy = map(int, raw_input().split())
        a.append(dummy)
    n = input()
    for i in range(4):
        dummy = map(int, raw_input().split())
        b.append(dummy)
    z = set(a[m-1])
    y = set(b[n-1])
    
    l = (z.intersection(y))
    if len(l)==0:
        print "Volunteer cheated!"
    elif len(l)==1:
        print l.pop()
    else:
        print "Bad magician!"
