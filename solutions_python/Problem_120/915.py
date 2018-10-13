c=input()
for x in range(1,c+1):
    count=0
    s=raw_input()
    s=[int(u) for u in s.split()]
    r=s[0]
    t=s[1]
    inc=2*r
    area=2*r+1
    c2=5
    while(area<=t):   
        count+=1
        area+=(inc+c2)
        c2+=4
    print 'Case #'+str(x)+': '+str(count)
