
n=int(input())

for nb in range(n):
    r,c=[int(i) for i in input().split()]
    data=[[e for e  in input()] for _ in range(r)]
    #print(data)
    for i in range(r):
        k=0
        for j in range(c):
            if data[i][j] !="?":
                for l in range(k,j):
                    data[i][l]=data[i][j]
                k=j+1
            else:
                pass
        if k!=0:
            for l in range(k,c):
                data[i][l]=data[i][k-1]

    k=0
    for i in range(r):
        if data[i][0] !="?":
            for l in range(k,i):
                data[l]=data[i]
            k=i+1
        else:
            pass
    if k!=0:
        for l in range(k,r):
            data[l]=data[k-1]

    #print(data)
    print("Case #"+str(nb+1)+":")
    for l in data:
        print("".join(l))

"""
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
"""
