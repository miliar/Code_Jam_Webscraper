def st(l):
    # print l
    while l[0]==0:
        l.pop(0)
    return l
def f(x,l):
    pre=0
    for c,i in enumerate(l):
        if i>=pre:
            pre=i
        else:
            a=False
            c-=1;
            while c>0:
                if l[c]>l[c-1]:
                    break
                c-=1
            l[c]-=1
            c+=1
            while c<len(l):
                l[c]=9
                c+=1
            break
    # print l
    return l
for c in range(int(raw_input())):
    n=map(int,raw_input().strip())
    print "Case #{}: {}".format(str(c+1),"".join(map(str,st(f(0,n)))))
