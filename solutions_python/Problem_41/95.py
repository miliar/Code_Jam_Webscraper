def main():
    f=open("gogogo.in","r")
    lines=f.readlines()
    outfile = open("test_result.out", 'w')
    T=int(lines[0][:-1])
    for i in xrange(1,T+1):
        lista=gen(lines[i][:-1])
        nx=next(lista)
        no=ungen(nx)
        print "Case #" +str(i)+": "+str(no)
        outfile.write('Case #'+str(i)+': '+str(no)+'\n')
        
        


def next(lista):
    n=len(lista)
    if n==1:
        lista.append(0)
        return lista
    for i in xrange(n-2,-1,-1):
        for j in xrange(n-1,i,-1):
            if lista[i]<lista[j]:
                a=lista[j]
                lista[j]=lista[i]
                lista[i]=a
                z=lista[i+1:n]
                z.sort()
                return lista[:i+1]+z
    count=0
    l=[]
    t=len(lista)
    for i in xrange(t):
        if lista[i]!=0:
            l.append(lista[i])
        else:
            count+=1
    l.sort()
    lista=[l[0]]+[0]*(count+1)+list(l[1:])
    return lista
    
                
def gen(string):
    lista=[]
    k=len(string)
    for i in xrange(k):
        lista.append(int(string[i]))
    return lista

def ungen(lista):
    string=""
    for i in lista:
        string+=str(i)
    return int(string)

if __name__ == "__main__":
    main()
        

