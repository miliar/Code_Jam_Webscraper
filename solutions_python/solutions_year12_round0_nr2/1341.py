f = open("B-small-attempt2.in", 'r')
f1 = open("dancing.out", 'w')
num = int(f.readline())
count = 0

for i in f:
    count+=1
    ct = 0
    i = i.rstrip('\n')
    ls = i.split()
    N = int(ls[0])
    S = int(ls[1])
    p = int(ls[2])
    ls = ls[3:]
    for t in ls:
        t = int(t)
        if t < 3:
            if t>= p:
                if t==2 and S>0:
                    S-=1
                    ct+=1
                elif t!=2:
                    ct+=1
            continue
        div = round(t/3.0)
        if div >=p:
            ct+=1
        elif t%3 == 1 and div+1 >= p:
            ct+=1
        elif S>0 and div+1 >= p:
            ct+=1
            S-=1
    f1.write("Case #"+str(count)+": "+str(ct)+"\n")
    
    
