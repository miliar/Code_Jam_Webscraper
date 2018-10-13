a=int(input())
for i in range(a):
    b=int(input())
    while(True):
        s=str(b)
        s=list(s)
        sorted_list=sorted(s)
        if(s==sorted_list):
            break
        else:
            b-=1
    print("Case #%d: %d" % (i+1,b))
