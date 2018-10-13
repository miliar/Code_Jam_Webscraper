def is_happy(strg):
    for i in range(0,len(strg)):
        if strg[i] == "-":
            return i
    return -1

def invert(k):
    if k=="+":
        return "-"
    else:
        return "+"

def solve(strg,cnt):
    global z
    res=is_happy(strg)
    if res==-1:
        print("Case #{}: {}".format(z,cnt))
        return
    else:
        if (res+flip)<=top:
            for i in range(res,flip+res):
                strg[i]=invert(strg[i])
            solve(strg,cnt+1)
        else:
            print("Case #{}: {}".format(z, "IMPOSSIBLE"))
            return
#main loop
num=int(input())
ct2=1
for z in range(1, num+1):
    strg,flip=map(str,input().strip().split(" "))
    flip=int(flip)
    strg=list(strg)
    top = len(strg)
    cnt = 0
    solve(strg, cnt)