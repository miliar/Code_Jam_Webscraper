def es(n,s):
    res=False
    for i in xrange(1,len(n)+1):
    #for i in range(len(n),0,-1):
        t = n[-i:]
        c = n[:-i]
        #print t + c + "==" + s + "?"
        if (t+c)==s:
            res=True;
    return res

def contar(n,m):
    cont=0
    t2 = n
    r = int(n)
    r1 = int(m)
    for i in xrange(r,r1 +1):
        for j in xrange (r,r1 + 1):
            if (int(t2)!=i and es(t2,str(i))):
                cont+=1
            t2 = str(int(t2)+1)
        t2= n
    return cont/2

def main():
    c= int(raw_input())
    for i in xrange (1,c+1):
        a,b = raw_input().split()
        if (a==b):
            print "Case #" + str(i) + ": "+"0"
        else:
            print "Case #" + str(i) + ": "+str(contar(a,b))
main()
