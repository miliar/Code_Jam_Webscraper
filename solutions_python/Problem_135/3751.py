foo = open("input.in",'r')
bar = open("output.in",'w')
t = int(foo.readline().strip())
i=1
while t>0:
    ch1 = int(foo.readline().strip())

    
    r1 = foo.readline().strip().split()
    r2 = foo.readline().strip().split()
    r3 = foo.readline().strip().split()
    r4 = foo.readline().strip().split()

    ch2 = int(foo.readline().strip())
    p1 = foo.readline().strip().split()
    p2 = foo.readline().strip().split()
    p3 = foo.readline().strip().split()
    p4 = foo.readline().strip().split()

    f1 = [r1,r2,r3,r4]
    f2 = [p1,p2,p3,p4]

    t1 = f1[ch1-1]
    t2 = f2[ch2-1]

    count = 0
    for each in t1:
        if each in t2:
            card = each
            count += 1

    if count==0:
        msg = "Volunteer cheated!"
    elif count==1:
        msg = card
    else:
        msg = "Bad magician!"
        
    res = "Case #"+str(i)+": "+msg
    print res
    bar.write(res+'\n')
    i+=1
    
    t-=1

bar.close()
foo.close()
