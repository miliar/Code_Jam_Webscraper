z=open("sample.txt","r")
w=open("output.txt","w")

x=int(z.readline())

for case in range(1,x+1):
    time=float(0)
    cr=float(2)
    c,f,x=z.readline().split()
    c=float(c)
    f=float(f)
    x=float(x)
    while True:
        taken=round((x/cr),8)
        ctaken=round((c/cr)+(x/(cr+f)),8)
        if taken<ctaken or abs(ctaken-taken)<pow(10,-8):
            time+=taken
            break
        elif ctaken<taken:
            time+=(c/cr)
            cr+=f
    w.write("Case #%d: %.9f\n" %(case,time))
w.close()
z.close()
     
