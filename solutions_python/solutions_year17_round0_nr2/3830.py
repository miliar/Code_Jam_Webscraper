path = "Scripts/Fun/CodeJam/"
filename = "Downloads/B-large.in";
X = open(filename).readlines();

Y = open(path+"output2.txt","w+");

T = int(X[0]);

for t in range(1,T+1):
    X[t] = X[t].strip();
    n = len(X[t])
    for i in range(n-1):
        if X[t][i] > X[t][i+1]:
            while X[t][i] == X[t][i-1] and i>0:
                i-=1;
            X[t] = int(X[t]);
            X[t] = X[t] / pow(10,n-i-1);
            X[t] *= pow(10,n-i-1);
            X[t] -= 1;
            break
    print "Case #"+str(t)+": "+str(X[t]);
    Y.write("Case #"+str(t)+": "+str(X[t])+"\n");

Y.close()
