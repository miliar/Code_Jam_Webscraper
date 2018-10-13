f = open('tempA1','r')
c = 0
cd = 0
a = []

def solve(a,cd):
    ic = 0
    c = 0
    for i in a:
        for j in a[c:]:
            if i[0]<j[0] and i[1]>j[1]:
                ic = ic + 1
            elif i[0]>j[0] and i[1]<j[1]:
                ic = ic + 1
        c = c + 1
    print "Case #%d: %d" % (cd,ic,)
    return 0

for r in f:
    d = [int(k) for k in r.strip('\n').split(' ')]
    if c!=0 and len(d)==1:
        if cd!=0:
            solve(a,cd)  
        a=[]
        cd = cd + 1
    elif c!=0 and len(d)==2:
        a.append(d)
    c = c + 1
solve(a,cd)
f.close()
