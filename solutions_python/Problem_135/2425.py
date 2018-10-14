T=int(raw_input())
for Ti in range(0,T):
    f1=int(raw_input())
    for k in range(0,f1-1):
        raw_input()
    qwe1=raw_input().split(" ")
    for j in range(f1,4):
        raw_input()

    f2=int(raw_input())
    for k in range(0,f2-1):
        raw_input()
    qwe2=raw_input().split(" ")
    for j in range(f2,4):
        raw_input()

    #print qwe1,qwe2
    res=set(qwe1) & set(qwe2)
    res=list(res)
    if(len(res)==0):
        res="Volunteer cheated!"
    elif(len(res)>1):
        res="Bad magician!"
    else:
        res=res[0]
    print "Case #%d: %s"%(Ti+1,res)
print ""
