import re
fin = open(input('input file:'))
fout = open(input('output file:'),'w')
l,d,n = tuple(int(s) for s in fin.readline().split())
words = tuple(fin.readline() for i in range(d))
for i in range(n):
    r = re.compile(fin.readline().replace('(','[').replace(')',']'))
    c = sum( 1 for w in words if r.match(w))
    fout.write('Case #'+str(i+1)+": "+ str(c)+ "\n")
fin.close()
fout.close()
