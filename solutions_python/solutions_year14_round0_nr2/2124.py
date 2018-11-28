fin=open('B-large.in', 'r')
fout=open('result','w')
for i in range(int(fin.readline())):
    c,f,x=map(float, fin.readline().split())
    n,t=2,0
    while(True):
        s1=x/n
        s2=c/n+x/(n+f)
        if (s1 < s2):
            t+=s1
            break
        else:
            t+=c/n
            n+=f
    fout.write('Case #%d: %.7f\n' % (i+1, t))