def doProb(fname, ofname):
    f = open(fname, 'r');
    N = int(f.readline());
    of = open(ofname, 'w');

    s = ['Case #' + str(j) + ': ' + str(solve(int(f.readline()))) + '\n' for j in range(1,N+1)];
    of.writelines(s);    
    f.close();
    of.close();

def solve(N):
    nck = [[0 for i in range(N+1)] for i in range(N+1)];
    pos = [[0 for i in range(N+1)] for i in range(N+1)];

    #set up the nck grid first
    for i in range(N+1):
        nck[i][0] = 1;

    for i in range(1,N+1):
        for j in range(1,i+1):            
            nck[i][j] = nck[i-1][j] + nck[i-1][j-1];

    #set up the pos grid now

    for i in range(1,N+1):
        pos[i][1] = 1;
    
    for i in range(2,N+1):
        for j in range(2,i):
            for k in range(1,j):
                if(i-j-1<j-k-1):
                    continue;
                pos[i][j]+= pos[j][k]*nck[i-j-1][j-1-k];

    #solve the problem
    
    tot = 0;
    for i in range(1, N+1):
        tot += pos[N][i];
        
    return tot%100003;
