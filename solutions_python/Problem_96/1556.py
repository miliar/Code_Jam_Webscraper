f = open("in.txt", "r")
out = open("out.txt", "w")
cases = int(f.readline())
case = 0

for line in f:
    sol = 0
    x = line.split()
    N = int(x[0])
    S = int(x[1])
    p = int(x[2])

    sums = []
    divs = []
    mods = []
    for i in range(N):
        sums.append(int(x[i+3]))
        divs.append(int(x[i+3]) /3)
        mods.append(int(x[i+3]) %3)

    for i in sums:
        if (i%3) == 0:
            if (i/3) >= p:
                sol=sol+1
            elif ((i/3)+1 >= p) and (S>0) and (((i/3)-1) > 0):
                sol=sol+1
                S = S-1
        if (i%3) == 1:
            if (i/3)+1 >= p:
                sol=sol+1
        if (i%3) == 2:
            if ((i/3)+1 >= p):
                sol=sol+1
            elif ((i/3)+2 >= p) and (S>0):
                sol =sol+1
                S =S-1

    case=case+1
    out.write("Case #"+str(case)+": "+str(sol)+"\n")
    
                
