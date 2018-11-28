fh=open('js-large2.in','r')
gh=open('js-large2.out','w')
T=int(fh.readline())
for num in range(1,101):
    s='Case #'+str(num)+': '
    lst=fh.readline().split()
    lst1=list(map(float,lst))
    C=lst1[0]
    F=lst1[1]
    X=lst1[2]
    rate=2.0
    toMake=X
    elapsed=0
    while True:
        if (toMake/rate)<=(C/rate)+(toMake/(rate+F)):
            ans=elapsed+(toMake/rate)
            break
        elapsed+=C/rate
        rate+=F
    gh.write(s+str(ans)+'\n')
fh.close()
gh.close()