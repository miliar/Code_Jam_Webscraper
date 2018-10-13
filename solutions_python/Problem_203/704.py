def func(r,c,inp1):
    for i in range(r):
        for j in range(c):
            #print i,j
            for k in range(c):
                if((i < r-1) and (j == k)and ( inp1[i][j] != 63) and inp1[i+1][j] == 63):
                   # print "hello"
                    x = inp1[i][j]
                    inp1[i+1][j] = inp1[i][j]

    return inp1

def func2(r,c,inp1):
    for i in range(r):
        for j in range(c):
            for k in range(c):
                if((i < r-1) and (j == k)and ( inp1[i][j] != 63) and inp1[i+1][j] == 63):
                    x = inp1[i][j]
                    inp1[i+1][j] = inp1[i][j]

    return inp1

    
t = int(raw_input())
for m in range(t):
    r,c = raw_input().split()
    r,c = [int(r),int(c)]
    inp = []
    for i in range(r):
        str = raw_input()
        inp.append(map(ord,list(str)))
    inp1 = inp
    w = 0
    x = func(r,c,inp1)
    # for i in range(r):
    #     print (map(chr,x[i]))
    inp1 = inp1[::-1]
    x = func(r,c,inp1)
    x = x[::-1]
    x = map(list, zip(*x))
    x = func2(c,r,x)
    x = x[::-1]
    x = func2(c,r,x)
    x = x[::-1]
    x = map(list, zip(*x))
    ans = []
    for i in range(r):
        ans.append(''.join(map(chr,x[i])))
    ans=  '\n'.join(ans)
    ans = '\n' + ans
    print "Case #{}: {}".format(m+1,ans)

