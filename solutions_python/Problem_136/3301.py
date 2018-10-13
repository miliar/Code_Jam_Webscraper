from sys import stdin
fi=open('input.txt','r')
#fi=open('inputs.txt','r')
fo=open('output.txt','w')
t=int(fi.readline())
for T in xrange(1,t+1):
    c,f,x=map(float,fi.readline().split())
    tym=0
    best=x/2
    inc=2.0
    while tym<=best:
        tym+=c/inc
        inc+=f
        best=min(best,tym+x/inc)
    s='Case #'+str(T)+': '
    fo.write(s+format('%.7f'%best)+'\n')
fi.close()
fo.close()
