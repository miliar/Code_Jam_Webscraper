#conso
def combi(iter,p):
    l=[]
    for i in xrange(len(iter)-p):
        l.append(iter[i:i+p+1])
    return l

def count(iter,n):
    c=0
    for p in xrange(len(iter)+1):
        v=['a','e','i','o','u']
        for i in combi(iter,p):
            temp=0
            final=0
            for j in xrange(len(i)):
                if i[j] not in v:
                    temp+=1
                else:
                    final=max(final,temp)
                    temp=0
            final=max(final,temp)
            if final>=n:
                c+=1
    return c
        
    
infile=open("A-small-attempt0.in",'r')
outfile=open("Consonants",'w')
lines=infile.readlines()
infile.close()
t=int(lines[0][:-1])
for i in xrange(t):
    s,n=[j for j in lines[i+1][:-1].strip().split()]
    n=int(n)
    outfile.write("Case #"+str(i+1)+": "+str(count(s,n))+"\n")
outfile.close()
