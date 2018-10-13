f = open('input.txt','rt');
f1 = open('output.txt','wt')
n = int(f.readline())
for i in xrange(n):
    f.readline()
    a=map(int,f.readline().split(' '))
    b=map(int,f.readline().split(' '))
    a.sort()
    b.sort(lambda x,y:cmp(y,x))
    f1.write("Case #%d: %d\n"%(i+1,reduce(lambda x,y:x+y[0]*y[1],zip(a,b),0)))
