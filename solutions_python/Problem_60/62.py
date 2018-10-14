def doProb(fname, ofname):
    #do problem 3 given a file name
    f = open(fname, 'r');
    T = int(f.readline());
    output = ['Case #' + str(i) + ': '+ \
              solve([int(j) for j in f.readline().split()], [int(j) for j in f.readline().split()], [int(j) for j in f.readline().split()]) + \
              '\n' for i in range(1,T+1)];
    f.close();
    of = open(ofname, 'w');
    of.writelines(output);
    of.close();
    

def solve(Parms,X,V):
    #step 1: work out Hindered positions/other
    [N,K,B,T] = Parms;
    UH = [X[i]+V[i]*T >= B for i in range(N)];
    sm = sum(UH);
    if(sm<K):
        return 'IMPOSSIBLE';
    
    tot = 0;
    for start in range(N):
        tot += UH[start];
        if(tot>(sm-K)):
            break

    ret = 0;
    tot = 0;
    for j in range(start,N):
        if(UH[j]):
            tot+=1;
        else:
            ret+=tot;
    return str(ret);
