test=input()

for index in range(test):
    a=[]
    b=[]
    
    r=input()
    
    for j in range(4):
        a.append(raw_input().split())
    c=input()

    for j in range(4):
        b.append(raw_input().split())
        


    m1=a[r-1]
    m2=b[c-1]
    count=0
    element=""
    for i in m1:
        if i in m2:
            count+=1
            element=i

    if count==0:
        print "Case #%d:"%(index+1),"Volunteer cheated!"
    elif count==1:
        print "Case #%d: %s"%(index+1,element)
    else:
        print "Case #%d:"%(index+1),"Bad magician!"