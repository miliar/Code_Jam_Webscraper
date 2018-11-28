__author__ = 'lex'
input=open("int","r")
out=open("out","w")
n=int(input.readline())
for s in xrange(n):
    m=int(input.readline())
    line = input.readline()
    line=line[:-1]
    line=line.split(' ')
    line=[int(x) for x in line]
    summ=0
    if reduce(lambda x,y: x^y,line)==0:
        summ=sum(line)-min(line)
        out.write('Case #%s: %s\n' %((s+1).__str__(),summ.__str__()))
    else: out.write('Case #%s: NO\n' %((s+1).__str__()))


  