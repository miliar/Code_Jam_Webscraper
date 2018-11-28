#import os

path = "Scripts/Fun/CodeJam/"
filename = path+"A-small-attempt2.in";
X = open(filename).readlines();

Y = open(path+"output1.txt","w+");

T = int(X[0]);

for t in range(1,T+1):
    s = X[t];
    s = s.split()
    k = int(s[1]);
    m = [0 for i in range(len(s[0]))];
    for i in range(len(s[0])):
        if s[0][i] == '+':
            m[i]=1;
    c = 0;

    for i in range(len(s[0])-k+1):
        if m[i]== 0:
            for j in range(k):
                m[i+j]+=1;
                m[i+j]%=2;
            c+=1;

            
    if m[-k:] == [1 for i in range(k)]:
        print "Case #"+str(t)+": "+str(c);
        Y.write("Case #"+str(t)+": "+str(c)+"\n");
    else:
        print "Case #"+str(t)+": IMPOSSIBLE";
        Y.write("Case #"+str(t)+": IMPOSSIBLE\n");

Y.close();
