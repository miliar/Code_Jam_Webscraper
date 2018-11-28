txtin="A-large.in" # txtin="in.txt"
foutn="out.txt"
f = open(txtin,'r')
q=int(f.readline())

with open(foutn, 'w') as fout:
    for case in range(q):
        strr=f.readline()
        s,s2=strr.split()
        k = int(s2) #pancakeflipper
        p = []
        for c in s:
            p.append(-1 if c == '-' else +1)
        print (p)
        n = 0
        i = 0
        t = len(p)-k+1
        while i<t:
            if p[i]==-1:
                l=0
                while l<k:
                    p[i+l]=p[i+l]*-1
                    l=l+1
                n=n+1
            i=i+1
        print (n)
        ok=True
        for z in range(k):
            if p[-1-z]==-1:
                ok=False
                break
        if ok:
            fout.write('Case #'+str(case+1)+': '+str(n)+'\n')
        else:
            fout.write('Case #'+str(case+1)+': IMPOSSIBLE\n')   
print ('Fin')