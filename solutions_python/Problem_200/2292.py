def tidy(N, z):
    print N
    print z
    Nint = int("".join(N[0:z]))
    Nint -= 1
    Nl = list(str(Nint))
    
    for p in range(len(N)-z):
        
        Nl.append('9')
    return Nl



fileout = open('B-large.out',"w")

with open('B-large.in') as file:
    T = int(file.readline())
    
    for case in range(1, T + 1):
        N = list(file.readline().strip())
        unsorted = N
        N = sorted(N)
        
        while unsorted != N:
            for i,x in enumerate(unsorted):
                if unsorted[i+1] < unsorted[i]:
                    N = tidy(unsorted,i + 1)
                    break
                
            unsorted = N
            N = sorted(N)
            print(unsorted)
        ans = int("".join(unsorted))
        fileout.write("Case #" + str(case) + ": " + str(ans) + "\n")
    
fileout.close()

        
        