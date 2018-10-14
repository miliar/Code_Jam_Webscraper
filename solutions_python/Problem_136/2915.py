f = open("B-large.in",'r')
o = open("B-large.out",'w');

def click(C,F,X):
    solved=False
    n = 2.0
    t = 0.0
    while not solved:
        r = X/n
        r_next= X/(n+F)
        factory_time= C/n
##        print ( r,r_next, factory_time);
        if(r<=(r_next+factory_time)):
            t+=r
            solved=True
        else:
            t+=factory_time
            n+=F;
    return round(t,7)


t = int(f.readline())

for c in range(t):
    vs=[float(r) for r in f.readline().split()]
    answer= click(vs[0],vs[1],vs[2])
    o.write("Case #%d: %.7f" %(c+1,answer)+"\n")
f.close()
o.close()
