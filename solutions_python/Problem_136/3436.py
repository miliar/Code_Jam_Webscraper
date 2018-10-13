in1 = open ("p2.in", "r");
out1 = open ("p2.out","w");
testCases = int(in1.readline());
for j in range (1, testCases+1):
    cfx = in1.readline().split();
    c = float (cfx[0]);
    f = float (cfx[1]);
    x = float (cfx[2]);
    lowestTime=100000/2;
    n=1;
    currTime = x/2;
    while(currTime < lowestTime):
        lowestTime=currTime;
        currTime=0;
        for i in range (0,n):
            currTime+=c/(2+f*i);
        currTime+=x/(2+f*n);
        n+=1;
    out1.write("Case #"+ str(j) + ": " + str(lowestTime)+"\n");
out1.close();
