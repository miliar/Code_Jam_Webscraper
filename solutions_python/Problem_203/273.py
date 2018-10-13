T = int(input())
for t in range(1,T+1):
    r, c = [int(s) for s in input().split(' ')]
    tab = []
    for i in range(r):
        tab.append(list(input()))

    for i in range(r):
        for j in range(c):
            if tab[i][j]=='?':
                if j>0 and tab[i][j-1]!='?':
                    tab[i][j]=tab[i][j-1]
                    #print(tab)
                else:
                    k = j+1
                    while k < c and tab[i][k]=='?':
                        k+=1
                    #print('k=',k)
                    if k<c:
                        for a in range(j,k):
                            tab[i][a]=tab[i][k]
                    elif i>0 and '?' not in tab[i-1]:
                        tab[i]=tab[i-1]
    i = r-1
    while i>=0:
        if '?' in tab[i]:
            tab[i] = tab[i+1]
        i-=1

    print('Case #'+str(t)+':')

    for i in range(r):
        print(''.join(tab[i]))
