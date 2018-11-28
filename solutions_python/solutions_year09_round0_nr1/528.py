import re
f=open('A-large.in','r')
length,size,cases=map(int,f.readline().rsplit())
dicc=''.join([f.readline() for i in range(size)])
results=[re.subn(f.readline().replace('(','[').replace(')',']'), '', dicc)[1] for i in range(cases)]
out=open('A-large.out','w')
out.write('\n'.join(["Case #"+str(i+1)+": "+str(results[i]) for i in range(len(results))]))
