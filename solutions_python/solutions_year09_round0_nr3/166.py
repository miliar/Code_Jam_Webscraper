def calculate(long):
    short = "welcome to code jam"
    
    if (len(long)<len(short)):
        return 0
    
    A = []
    N = len(long)
    M = len(short)
    for i in range(M):
        tmp = range(N)
        for j in range(N):
            tmp[j] = 0
        A.append(tmp)
    
    j = N - 1
    sum = 0
    while (j>=0):
        if (short[M-1] == long [j]):
            sum = sum + 1
        A[M-1][j] = sum
        j = j - 1

    j = N-2
    while (j>=0):
        i = M-2
        while(i>=0):
            A[i][j] = A[i][j+1] + (short[i] == long[j])*A[i+1][j+1]
            i = i - 1
        j = j - 1


    return A[0][0]%10000


def main():
    f = open("./Desktop/C-large.in")
    g = open("./Desktop/output","w")
    
    numcases = int(f.readline())
    

    
    for case in range(numcases):
        long = f.readline()
        long = long[:-1]
        answer = str(calculate(long))

        st = "Case #" + str(case + 1) + ": " + answer.zfill(4) + "\n"
        g.write(st)        
        
        
        
        
