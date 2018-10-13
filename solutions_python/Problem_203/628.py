def find_road(cake,r,c):
    i = 0
    while i<r:
        j=0
        while j<c:
            if cake[i][j] != '?':
                h = i-1
                con = True
                while h>-1 and con:
                    if cake[h][j] == '?':
                        cake[h][j] = cake[i][j]
                        h-=1
                    else:
                        con = False
                h = i+1
                con = True 
                while h<r and con:
                    if cake[h][j] == '?':
                        cake[h][j] = cake[i][j]
                        h+=1
                    else:
                        con = False
            j+=1
        i+=1
    j = 0
    while j<c:
        if cake[0][j] == '?':
            if j>0:
                i = 0
                while i<r:
                    cake[i][j] = cake[i][j-1]
                    i+=1
            else:
                h = 1
                while cake[0][h] == '?':
                    h+=1
                i = 0
                while i<r:
                    cake[i][j] = cake[i][h]
                    i+=1
        j+=1
                

T = int(input())
i = int(0)
while i<T:
    print("Case #%i:"%(i+1))
    i+=1
    r,c = [int(e) for e in input().split()]
    cake =[]
    for e in range(r):
        row = []
        for k in input():
            row.append(k)
        cake.append(row)
    find_road(cake,r,c)
    for e in cake:
        for h in e:
            print(h,end="")
        print()
