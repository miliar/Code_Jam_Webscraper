def solve(al):
    change = 0
    al.sort()
    print(al)
    n = len(al)
    AtoA = []
    AtoB = 0
    At = 720
    Bt = 720
    for i in range(0,n):
        if al[i][2]:
            At -= al[i][1] - al[i][0]
        else:
            Bt -= al[i][1] - al[i][0]
        
        next = i + 1
        t = 0
        if i == n-1:
            next = 0
            t = al[next][0] + 24*60 - al[i][1]      
        else:
            t = al[next][0] - al[i][1]
            
        if al[i][2] != al[next][2]:
            AtoB += t
            change += 1
        elif al[i][2]:
            AtoA.append((t, True))
        else:
            AtoA.append((t, False))
    print( "AtoA", AtoA)
    print( "AtoB", AtoB)
    AtoA.sort()
    
    for a in AtoA:
        if a[1]: # BtoB
            if At >= a[0]:
                At -= a[1]
            else:
                change += 2
        else:
            if Bt >= a[0]:
                Bt -= a[1]
            else:
                change += 2
    
    return change
            
    

with open("B-small-attempt0.in", "r") as ifile, open("out.txt", "w") as ofile:
    lines = ifile.readlines()
    T = int(lines[0])
    li = 1
    for i in range(0, T):
        [AC,AJ] = map(int,lines[li].split(" "))
        li+=1
        al = []
        for j in range(0, AC):
            [start,end] = map(int,lines[li].split(" "))
            al.append((start,end,False))
            li+=1
        for j in range(0, AJ):
            [start,end] = map(int,lines[li].split(" "))
            al.append((start,end,True))
            li+=1
        ofile.write("Case #{}: {}\n".format(i+1, solve(al)))
        
        