__author__ = 'sia'

n=int(raw_input())
for i in range(n):
    a,b=raw_input().split(" ")
    c=map(int,b)
    # print c
    res=0
    standing=c[0]
    for j in range(1,len(c)):
        if standing>=j:
            standing+=c[j]
        elif c[j]!=0:
            res+=j-standing
            standing+=j-standing+c[j]
        # print j,c[j],res,standing
    print "Case #%d: %d"%(i+1,res)



