fin=open('input.txt', 'r')
fout=open('output.txt', 'w')

def check(x,y):
    if len(x)==2:
        if x[1:]+x[:1]==y: return 1
    elif len(x)==3:
        if x[1:]+x[:1]==y or x[2:]+x[:2]==y: return 1
    elif len(x)==4:
        if x[1:]+x[:1]==y or x[2:]+x[:2]==y or x[3:]+x[:3]==y: return 1
    return 0

t=int(fin.readline())
for i in range(t):
    l, r= map(int, fin.readline().split())
    res=0
    for x in range(l,r):
        for y in range(x+1,r+1):
	     if check(str(x),str(y)): res += 1
    fout.write('Case #'+str(i+1)+': '+str(res)+'\n')