import math

inp = open("C:/Users/Mariusz/Desktop/input.txt","r")
out = open("C:/Users/Mariusz/Desktop/output.txt","w")


def d(a,b):
    return [int(math.ceil(math.sqrt(a))),int(math.floor(math.sqrt(b)))]


def hit(n):
    if n%2 == 0:
        if n ==2:
            return 2
        elif n ==4:
            return 3
        elif n==6 :
            return 5
        else:
            return 2 + (n/2-1) + 0.5*(n/2-2)*(n/2-1) + ((n/2-3)*(n/2-2)*(n/2-1))/6
            
    if n%2 ==1:
        if n ==1:
            return 3
        elif n==3:
            return 5
        elif n == 5:
            return 8
        elif n == 7:
            return 13
        else:
            return 5 + 3*(n/2-1) + 2*(0.5*(n/2-2)*(n/2-1)+((n/2-3)*(n/2-2)*(n/2-1))/6)    



def trzyJedynki(n):
    a = n*[0]
    a[0]=1
    res=[]
    for i in range(1,len(a)-2):
        a[i] = 1
        for j in range(1,len(a)-1-i):
            a[i+1]= 1
            for k in range(1,len(a)-i-j):
                a[i+j+k] = 1
                b = []
                for e in a:
                    b.append(e)
                res.append([str(x) for x in b])
                a[i+j+k]=0
            a[i+j]=0
        a[i]=0
    return res



def dwieJedynki(n):
    a = n*[0]
    a[0]=1
    res=[]
    for i in range(1,len(a)):
        a[i] = 1
        for j in range(len(a)-1-i):
            a[len(a)-1-j] = 1
            b = []
            for e in a:
                b.append(e)
            res.append([str(x) for x in b])
            a[len(a)-1-j] = 0
        a[i]=0
    return res



def jednaJedynka(n):
    a = n*[0]
    a[0]=1
    res=[]
    for i in range(1,len(a)):
        a[i] = 1
        b = []
        for e in a:
            b.append(e)
        res.append([str(x) for x in b])
        a[i] = 0
    return res

def dwojki(n):
    if n%2 == 0:
        return [int('2'+(n-2)*'0'+'2')]
    else:
        return [int('2'+(n-2)*'0'+'2'),int('2'+(n-2)/2*'0'+'1'++(n-2)/2*'0'+'2') ]





def gen(n):
    if n ==1:
        return [1,2,3]
    elif n==2:
        return [11,22]
    elif n==3:
        return [101,111,121,202,212]
    elif n==4:
        return [1001,1111,2002]
    else:
        res = []
        res.append(int('1'+(n-2)*'0'+'1'))
        res += dwojki(n)
        if n%2 == 0:
            w = jednaJedynka(n/2)
            r = dwieJedynki(n/2)
            t  = trzyJedynki(n/2)
            for e in w+r+t:
                x = []
                for f in e:
                    x.append(f)
                e.reverse()
                s = x+e
                res.append(int(''.join(s)))
            return res
        elif n%2 ==1:
            res.append(int('1'+(n-2)/2*'0'+'1'+(n-2)/2*'0'+'1'))
            res.append(int('1'+(n-2)/2*'0'+'2'+(n-2)/2*'0'+'1'))
            w = jednaJedynka(n/2)
            r = dwieJedynki(n/2)
            t  = trzyJedynki(n/2)
            for e in w+r+t:
                x = []
                for f in e:
                    x.append(f)
                e.reverse()
                p = ['0','1']
                for licz in p:
                    s = x+[licz]+e
                    res.append(int(''.join(s)))
            for e in jednaJedynka(n/2):
                x = []
                for f in e:
                    x.append(f)
                e.reverse()
                s = x + ['2'] + e
                res.append(int(''.join(s)))
            
            return res
            
            

T = int(inp.readline()[:-1])
for i in range(1,T+1):
    w = inp.readline()[:-1].split()
    prz=d(int(w[0]),int(w[1]))
    pal = []
    for j in range(len(str(prz[0])), len(str(prz[1]))+1):
        pal += gen(j)

    counter = 0
    for e in pal:
        if e**2 >=int(w[0])and e**2 <= int(w[1]):
            counter +=1
    out.write("Case #{0}: {1}".format(i, counter)+'\n')



out.close()
inp.close()



