maxt = 999999
import time
start_time = time.clock()


##def palin(string): #1 if palin
##    ln = len(string)
##    i = 0
##    j = ln-1
##
##    while(i<j):
##        if string[i]!=string[j]:
##            return 0
##        i+=1
##        j-=1
##        
##    return 1

##tota=0
##for i in range(1,maxt):
##    gen = str(i)
##    ln = len(gen)
##
##    gen1 = gen
##    gen2 = gen
##
##    for j in range(ln):
##        gen1+=gen[ln-j-1] #whole even flip
##
##    for j in range(ln-1):
##        gen2+=gen[ln-j-2] #whole odd flip
##
##    gent1 = str(int(gen1)**2)
##    gent2 = str(int(gen2)**2)
##
##    if palin(gent1):
##        tota+=1
##        #print(gen1)
##    if palin(gent2):
##        tota+=1
##        #print(gen2)
##print(tota)

def fsq(t,s,n): #total sum at most s>=0, n digits, how many?
    #t=1 if start of word, else 0
    tot = 0
    if n==2:
        for i in range(t,10):
            if 2*(i**2)<=s:
                tot+=1
            else:
                break
        return tot
    if n==1:
        for i in range(t,10):
            if i**2<=s:
                tot+=1
            else:
                break
        return tot

    #so n>=3
    for i in range(t,10):
        if 2*(i**2)<=s:
            tot += fsq(0,s-2*(i**2),n-2)
        else:
            break
    return tot

#print(fsq(1,9,4))
    

def rfsq(a,b,s,n): #[a,b],total sum at most s, n digits, how many?
    tot=0
    a = list(a)
    b = list(b)


    if n==2:
        m = 10*int(a[0])+int(a[1])
        n = 10*int(b[0])+int(b[1])
        for i in range(int(a[0]),10):
            if 11*i<=n:
                if m<=11*i and 2*(i**2)<=s:
                    tot+=1
            else:
                break
        return tot
    if n==1:
        for i in range(int(a[0]),10):#0,3
            if i**2<=s and i<=int(b[0]):
                tot+=1
            else:
                return tot
    #so n>=3
    for i in range(int(a[0]),10):
        if 2*(i**2)<=s and i<=int(b[0]):

            if i==int(b[0]):
                go = 1
                
                d = b[:]
                del(d[n-1])
                del(d[0])

                if(i>int(b[n-1])):
                    j=n-3
                    
                    while j>=0:
                        if int(d[j])!=0:
                            d[j] = str(int(d[j])-1)
                            go = 1
                            break
                        else:
                            d[j]=9
                            j-=1
                            go = 0 #go is only 0 if all 0's

                if i==int(a[0]):
                    c = a[:]
                    del(c[n-1])
                    del(c[0])
                    
                    if(i<int(a[n-1])):
                        j=n-3
                        if int(c[j])!=10-1:
                            c[j] = str(int(c[j])+1)
                else:
                    c = ""
                        
                    for j in range(n-2):
                        c+="0"

                if go:
                    tot+=rfsq(c,d,s-2*(i**2),n-2)
            
            elif i==int(a[0]):
                c = a[:]
                del(c[n-1])
                del(c[0])
                
                if(i<int(a[n-1])):
                    j=n-3
                    if int(c[j])!=10-1:
                        c[j] = str(int(c[j])+1) #process does not overcount unless s>=9^2 here as even if c ends in 9, no possible solutions have a 9 anyway

                d = ""
                for j in range(n-2):
                    d+="9"


                tot+=rfsq(c,d,s-2*(i**2),n-2)
            
            else:
                tot += fsq(0,s-2*(i**2),n-2)

    return tot

def ffsq(a,b):
    a = list(a)
    b = list(b)

    ln1 = len(a)
    ln2 = len(b)

    if ln1==ln2:
        return(rfsq(a,b,9,ln1))
    #so not
    tot = 0

    c = []
    for i in range(ln1):
        c.append("9")
    d = []
    for i in range(ln2):
        d.append("0")
    d[0]="1"

    tot += rfsq(a,c,9,ln1)
    tot += rfsq(d,b,9,ln2)

    for i in range(ln2-ln1-1):
        tot += fsq(1,9,ln1+1+i)
    return tot

def add(lst1, lst2):
    lst1 = lst1[::-1]
    lst2 = lst2[::-1]

    ln1 = len(lst1)
    ln2 = len(lst2)

    if ln1<ln2:
        for i in range(ln2-ln1):
            lst1+="0"
            ln1=ln2
    elif ln1>ln2:
        for i in range(ln1-ln2):
            lst2+="0"
            ln2=ln1

    res = ""
    rem = 0
    for i in range(ln1):
        a = int(lst1[i])+int(lst2[i])+rem
        res+=str(a%10)

        if a>=10:
            rem = 1
        else:
            rem = 0
    if rem:
        res+=str(rem)
    res=res[::-1]

    return res

def sub(lst1, lst2):
    lst1 = lst1[::-1]
    lst2 = lst2[::-1]

    ln1 = len(lst1)
    ln2 = len(lst2)

    if ln1<ln2:
        for i in range(ln2-ln1):
            lst1+="0"
            ln1=ln2
    elif ln1>ln2:
        for i in range(ln1-ln2):
            lst2+="0"
            ln2=ln1

    res = ""
    rem = 0
    for i in range(ln1):
        a = int(lst1[i])-int(lst2[i])+rem
        res+=str(a%10)

        if a<=-1:
            rem = -1
        else:
            rem = 0

    i=ln1-1
    while i>=0 and res[i]=="0":
        res = res[:-1]
        i-=1
        
        
    res=res[::-1]

    return res

def comp(lst1,lst2):
    lst1 = lst1[::-1]
    lst2 = lst2[::-1]

    ln1 = len(lst1)
    ln2 = len(lst2)

    if ln1<ln2:
        for i in range(ln2-ln1):
            lst1+="0"
            ln1=ln2
    elif ln1>ln2:
        for i in range(ln1-ln2):
            lst2+="0"
            ln2=ln1

    for i in range(ln1):
        if lst1[ln1-i-1]<lst2[ln2-i-1]:
            return -1
        if lst1[ln1-i-1]>lst2[ln2-i-1]:
            return 1
    return 0
    
def div(lst1,lst2):
    ln1 = len(lst1)
    ln2 = len(lst2)

    p=""
    
    shift = ln1-ln2

    while shift>=0:
        i=0
        bit = lst1[:ln1-shift]
        while comp(bit,lst2)>=0:
            bit = sub(bit,lst2)
            i+=1
        
        p += str(i)
        p = p[::-1]
        i = len(p)-1
        while i>=0 and p[i]=="0":
            p = p[:-1]
            i-=1
        p = p[::-1]

        lst1 = bit + lst1[ln1-shift:]
        ln1 = len(lst1)
        shift -= 1
    return [p,lst1]

def sqrt(lst):
    if comp(lst,"100000000")<=0:
        ln = len(lst)
        a = "1"
        for i in range(int(ln/2)):
            a += "0"
        
    else:
        ln = len(lst)
        k = int(ln/2) - 3

        d = int(lst[0:ln-2*k])
        d = d**(0.5)
        d = int(d)
        d = str(d)

        for i in range(k):
            d+="0"
        
        a = d

    b = lst[:]


    while not(comp(add(a,"1"),b)>=0 and comp(add(b,"1"),a)>=0):
        x = div(lst,a)[0]
        x = add(a,x)
        x = div(x,"2")[0]

        b = a
        a = x
        
    x = div(lst,a)[0]
    x = add(a,x)
    x = div(x,"2")[0]

    b = a
    a = x

    if comp(a,b)==1:
        a = b #take a the smaller one

    s = add(a,"1")
    if comp(div(lst,s)[0],s) >= 0:
        a=s

    r = div(lst,a)
    if comp(r[0],a)==1 or comp(r[1],"")==1:
        rem = 1
    else:
        rem = 0
    return [a,rem]

fin = open('in.in','r')
fout = open('output.txt','w')

abc = fin.read()
abc = abc.split()

ntst = int(abc[0])
j = 1

for i in range(ntst):
    a = sqrt(abc[j])
    b = sqrt(abc[j+1])[0]

    if a[1] != 0:
        a = add(a[0],"1")
    else:
        a = a[0]

    fout.write("Case #{}: {}".format(i+1,ffsq(a,b))+"\n")
    j+=2
    if(j%400==1):
        print(0)
    
fin.close()
fout.close()

print( time.clock() - start_time, "seconds")
