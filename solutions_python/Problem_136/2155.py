fin = file('in.txt','r')
fout = file('out.txt','w')

n = int(fin.readline())

#turns -= c/p, p+=f, good if(c/p + x/(p+f) > x/p)

for i in range(n):
    c,f,x = map(float,fin.readline().split(' '))
    p = 2.0
    time = 0.0
    while (c/p + x/(p+f)) <= x/p:
        time += c/p
        p += f
    time += x/p
    fout.write("Case #%d: %.7f\n"%(i+1,time))

fin.close()
fout.close()
    
