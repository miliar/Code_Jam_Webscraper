ts=100
with open("prob_1_input.txt", "r+") as txt:
    li=txt.readlines()
for i in range(ts):
    p=li[i+1]
    p=p.strip('\n')
    p=p.split(' ')
    a=p[0]
    b=p[1]
    ps=int(b[0])
    c=0
    for j in range(1,int(a)+1):
        if (ps>=j):
            ps=ps+int(b[j])
        else:
            c+=1
            ps=ps+int(b[j])+1
        
    print 'Case #%s:'%(i+1) ,c
