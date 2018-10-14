g=open("two2.in","r")
h=open("out1.txt","w")
n=int(g.readline())
for i in range(n):
    line=g.readline().split()
    c=float(line[0])
    f=float(line[1])
    x=float(line[2])
    rate=2.0
    time=0;
    cookies=0;
    while(((c/rate)+(x/(rate+f)))<(x/rate)):
        time+=(c/rate)
        rate+=f
    time+=(x/rate)
    string="Case #"+str(i+1)+": "+str(round(time,7))+"\n"
    h.write(string);
h.close()
g.close()
