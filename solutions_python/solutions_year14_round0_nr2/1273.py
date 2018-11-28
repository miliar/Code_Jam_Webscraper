fl=file("B-large.in","r")
fo=file("output.txt","w")
t=int(fl.readline())
for i in xrange(t):
    s=fl.readline()
    c,f,x=map(float,s.split())
    time=0.0000000
    rate=2
    while True:
        if x/rate<c/rate+x/(rate+f):
            time+=x/rate
            break
        time+=c/rate
        rate+=f
    fo.write("Case #%d: %.7f\n"%(i+1,round(time,7)))
fl.close()
fo.close()
