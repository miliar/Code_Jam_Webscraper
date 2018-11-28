from pprint import pprint
n=int(input())

for nb in range(n):
    n,p=[int(i) for i in input().split()]
    recipe=[int(i)for i in input().split()]
    q=[sorted([int(i)for i in input().split()])for i in range(n)]

    #pprint(recipe)
    #pprint(q)
    """for i in range(n):
        print(q[i][0]/recipe[i]*9/10)
        print(q[i][-1]/recipe[i]*11/10)
        for j in range(p):
            print(q[i][j]/recipe[i],end=" ")
        print()
    """
    for i in range(n):
        for j in range(p):
            q[i][j]=(int(q[i][j]*10/11/recipe[i]-0.0000001),int(q[i][j]*10/9/recipe[i]))
    #pprint(q)
    """
    s=[p-1]*n
    m=0
    while all(s[i]>=0 for i in range(n)):
        mi=min(q[i][s[i]][1] for i in range(n))
        ma=max(q[i][s[i]][0] for i in range(n))
        print(mi , ma)
        if mi > ma:
            m+=1
        else:
            pass
        s[0]-=1
    """


    m=0
    s=[0]*n
    while all(s[i]<p for i in range(n)):
        ma=max(q[i][s[i]][0] for i in range(n))
        mi=min(q[i][s[i]][1] for i in range(n))
        #print(s,ma,mi)
        if ma<mi:
            for i in range(n):
                s[i]+=1
            m+=1
        else:
            for i in range(n):
                while s[i]<p and ma>=q[i][s[i]][1]:
                    s[i]+=1


    print("Case #"+str(nb+1)+":",m)
"""
6
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
1 8
10
11 13 17 11 16 14 12 18
3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900
"""
