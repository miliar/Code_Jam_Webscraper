T = int(input())

def nconflict(a,b):
    if b==0:
        return True
    if a==b:
        return False
    if abs(a-b)==1:
        return False
    if abs(a-b)==5:
        return False
    return True

def place(c,l,s):
    inds = list(range(len(l)))
    inds = inds[s:] + inds[:s]
    for i in inds:
        ln = i-1
        rn = i+1
        if rn == len(l):
            rn = 0
        if l[i] == 0 and nconflict(c,l[ln]) and nconflict(c,l[rn]):
            l[i] = c
            return i
    return 0

cols = {1:'R',2:'O',3:'Y',4:'G',5:'B',6:'V'}
def convert(l):
    for i in range(len(l)):
        l[i] = cols[l[i]]

for c in range(T):
    colors = list(map(int,input().split()))
    N = colors[0]
    ans = [0]*N
    last = 0
    order = list(range(1,7))
    order.sort(key=lambda x: colors[x], reverse=True)
    for ti in order:
        while colors[ti] > 0:
            last = place(ti,ans,last)
            colors[ti] -= 1
    if 0 in ans:
        print('Case #',(c+1),': IMPOSSIBLE',sep='')
    else:
        convert(ans)
        print('Case #',(c+1),': ',*ans,sep='')
