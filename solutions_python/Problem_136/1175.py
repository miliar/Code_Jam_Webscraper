import sys
input_from_file=True
fout=open("G:/o.txt","w")
if input_from_file:
    f=open("G:/ab.txt","r")
else:
    f=sys.stdin
t=int(f.readline())
for i in range(t):
    s=f.readline()
    C,F,X=map(float,s.split())
    mmax=X/2.0
    ck=2
    t1=0
    while True:
        t1=t1+C/ck
        ck=ck+F
        t2=X/ck
        tt=t1+t2
        if tt>mmax:
            tt=mmax
            break
        else:
            mmax=tt
    output="Case #" + str(i) + ": " + str(round(tt,7)) + "\n"
    fout.write(output)
fout.close()
f.close()    



