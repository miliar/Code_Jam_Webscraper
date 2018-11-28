def googledancer(fileName, outputFileName):
    problem = open(fileName)
    output = open(outputFileName, 'a')
    line = problem.readline()
    T = int(line)
    
    i = 1
    while i <= T:
        line = problem.readline()
        inp = [int(n) for n in line.split()] 
        max = bestresults(inp)
        if i != T:
            output.write("Case #"+str(i)+": "+str(max)+"\n")
        else:
            output.write("Case #"+str(i)+": "+str(max))
        i+=1
                          
def bestresults(inp):
    N = inp[0]
    S = inp[1]
    p = inp[2]
    total = 0
    
    if(p == 0):
        return N
    
    i = 3
    while i<(3+N):
        score = inp[i]
        if(score != 0):
            if(score % 3 == 0):
                if(score/3 >= p):
                    total+=1
                elif((score/3+1) >= p  and  S > 0):
                    S-=1
                    total+=1
            if(score % 3 == 1):
                if((score/3+1) >= p):
                    total+=1
            if(score % 3 == 2):
                 if((score/3+1) >= p):
                    total+=1
                 elif((score/3+2) >= p and S > 0):
                    S-=1
                    total+=1
        i+=1
    return total
    
