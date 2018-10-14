for i in range(int(input())):
    s=[int(x) for x in input().split()]
    R=s[0]
    C=s[1]
    W=s[2]
    a=0
    if C%W==0:
        a=(C-W)/W+W
    else:
        y=(C-W)//W
        if y<1:
            a=1+W
        else:
            a=y+W+1
    print("Case #{}: {}".format(i+1,int(a)*R))
