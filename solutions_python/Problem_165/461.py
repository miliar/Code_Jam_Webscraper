
o = open("d.out","w")
for i in range(input()):
    r,c,w = map(int,raw_input().split())
    if w*2 <= c:
        tmp = w
        ans=0
        while c-tmp > w:
            tmp += w
            ans+=1
        ans += w+1
        if ans>c:
            ans = c
        ans *= r
        print r,c,w,ans
        o.write("Case #"+str((i+1))+": "+str(ans)+"\n")
    else:
        ans = w+1
        if ans > c:
            ans = c
        ans *= r
        print r,c,w,ans
        o.write("Case #"+str((i+1))+": "+str(ans)+"\n")
o.close()