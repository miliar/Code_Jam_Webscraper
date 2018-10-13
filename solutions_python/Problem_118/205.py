import sys

DIGITS = 26

fas = [0,1,4,9]
s = []
sz = 1

def work(x,ac):
    if x == sz:
        n = int("".join(s+s[::-1]))
        fas.append(n**2)
        i = 0
        while ac-i*i>=0:
            n = int("".join(s+[str(i)]+s[::-1]))
            fas.append(n**2)
            i += 1
        return
    for i in [1,2]:
        s[x]=str(i)
        if ac-i*i*2>=0:
            work(x+1,ac-i*i*2)
    s[x] = '0'
    if x > 0:
        work(x+1,ac)

while sz <= DIGITS:
    s = ['0']*sz
    work(0,9)
    sz += 1

fas.sort()
nums = len(fas)

def bs(x):
    l,r = [0,nums]
    while l+1<r:
        m = (l+r)/2
        if(fas[m]<=x):
            l = m
        else:
            r = m
    return l

tot_cases = int(sys.stdin.readline())
for case_num in range(1,tot_cases+1):
    a,b = [int(x) for x in sys.stdin.readline().split(" ")]
    i = bs(a)
    if fas[i] < a:
        i += 1
    j = bs(b)
    print "Case #%d: %d"%(case_num,max(0,j-i+1))
