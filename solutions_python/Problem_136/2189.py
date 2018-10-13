inf=open("B-large.in","r")
outf=open("cookieyay.txt","w")

for ab in range (int(inf.readline())):
    c,f,x=list(map(float,inf.readline().strip().split()))
    rate=2;
    time=0;
    mintime=10000000;
    count=0;
    buyingtime=0
    while True:
        time=0;
        #print("count:",count)
        if count>=1:
            buyingtime+=c/rate;
            rate=2+f*(count)
            
        
##        for i in range (count):
##            time+=c/rate
##            rate=2
##            #print("rate:",rate)
##        #print("time",time)
        time+=buyingtime;
        time+=x/rate
        count+=1;
        if mintime>time:
            mintime=time;
        
        else:
            break
    outf.write("Case #"+str(ab+1)+": ")
    outf.write(str(mintime)+"\n");
outf.close()
