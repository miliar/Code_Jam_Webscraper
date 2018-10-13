def solve(N,K,U,pl):
    if N == 0:
        return 1
        
    pl.sort()
    while U > 0.0 and pl[0] < 1.0:
        #print(U)
        #print(pl)
        cnt = 1
        nextP = 1.0
        for i in range(1, N):
            if pl[i] != pl[i-1]:
                nextP = pl[i]
                break
            cnt += 1
        inc = nextP-pl[0]
        #print(inc)
        if inc*cnt>=U:
            inc = U / cnt
            U = 0.0
        else:
            U-=inc*cnt
        #print(inc)
        for i in range(0, cnt):
            pl[i] += inc
        #print(pl)
            
    res = 1.0
    for p in pl:
        res *= p
        
    return res
        
    
            
            
            
        
            


with open("C-small-1-attempt1.in", "r") as ifile, open("out.txt", "w") as ofile:
    lines = ifile.readlines()
    T = int(lines[0])
    li = 1
    for i in range(0, T):
        [N,K] = map(int,lines[li].split(" "))
        li+=1
        U = float(lines[li])
        li+=1
        pl = [ float(x) for x in lines[li].split(" ")]
        li+=1
        ofile.write("Case #{}: {:0.6f}\n".format(i+1, solve(N,K,U,pl)))