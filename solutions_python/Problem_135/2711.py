n = int(input())
for ie in range(n):
    x1 = int(input())
    d = []
    for i in range(4):
        d.append([int(x) for x in input().split()])
    x2 = int(input())
    d1 = []
    for i in range(4):
        d1.append([int(x) for x in input().split()])   
    e1 = set(d[x1-1])
    e2 = set(d1[x2-1])
    ans = list(e1 & e2)
    #print(ans)
    if len(ans) == 1:
        print('case #%d: %d' % (ie+1,ans[0]))
    elif len(ans) > 0:
        print('case #%d: Bad magician!' % (ie+1))
    elif len(ans) == 0:
        print('case #%d: Volunteer cheated!' % (ie+1))