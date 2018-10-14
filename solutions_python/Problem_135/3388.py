fo=open('output.txt','w')
fi=open('input.txt','r')
t=int(fi.readline())

for _ in xrange(t):
    r1=int(fi.readline())
    a=[map(int,fi.readline().split()) for x in xrange(4)]
    se=set(a[r1-1])
    r1=int(fi.readline())
    a=[map(int,fi.readline().split()) for x in xrange(4)]
    se=se.intersection(set(a[r1-1]))
    s='Case #'+str(_+1)+':'+' '
    if len(se)==1:
        s+=str(se.pop())
    elif len(se)==0:
        s+='Volunteer cheated!'
    else:
        s+='Bad magician!'
    fo.write(s+'\n')
fi.close()
fo.close()

