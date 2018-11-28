h = input()
k = 0
while h>0:
    h -= 1
    k += 1
    n = input()
    s, t = [], []
    for i in range(4):
        s.append(raw_input().split())
    m = input()
    for i in range(4): 
        t.append(raw_input().split())
    c = 0
    ind = 0
    for i in range(4):
        for j in range(4):
            if s[n-1][i]==t[m-1][j]:
                c += 1
                ind = i
    if c==1:
       print "Case #%d: %s"%(k,s[n-1][ind])
    elif c==0:
       print "Case #%d: Volunteer cheated!"%k
    else:
       print "Case #%d: Bad magician!"%k
