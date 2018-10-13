def solve(file):
    f=open(file,"r")
    n=int(f.readline())
    for test in range(n):
        p1=[]
        p2=[]
        a1=int(f.readline())
        for x in range(4):
            p1.append(set(map(int,f.readline().split())))
        a2=int(f.readline())
        for y in range(4):
            p2.append(set(map(int,f.readline().split())))
        soln = p1[a1-1].intersection(p2[a2-1])
        out = "Case #"+str(test+1)+":"
        if len(soln) == 1:
            print out,soln.pop()
        elif len(soln) == 0:
            print out,"Volunteer cheated!"
        else:
            print out,"Bad magician!"
solve("input")
