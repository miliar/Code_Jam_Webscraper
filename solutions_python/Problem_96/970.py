#!/usr/bin/python -tt

def zerotuples(n):
    if n/3==0:
        return[(0,0,0)]
    if n/3+1>10:
        return[(10,10,10)]
    a = n/3,n/3,n/3
    b = n/3+1,n/3,n/3-1
    return [a,b]

def onetuples(n):
    if n/3==0:
        return [(n/3,n/3,n/3+1)]
    a =  n/3,n/3,n/3+1
    b = n/3+1,n/3+1,n/3-1
    return [a,b]

def twotuples(n):
    if n/3+2<=10:
        a =  n/3,n/3,n/3+2
        b = n/3+1,n/3+1,n/3
        return [a,b]
    else:
        return [(n/3+1,n/3+1,n/3)]

def surp(tuple):
    x = sorted(tuple)
    if x[0] +2 == x[1] or x[0]+2==x[2]:
        return True
    if x[1]+2==x[2]:
        return True
    return False

def greatern(tuple,n):
    for ele in tuple:
        if ele>=n:
            return True
    return False

def choice(tupleset,n):
    res = ()
    for ele in tupleset:
        s = surp(ele)
        g = greatern(ele,n)
        if len(res)==0:
            res=(ele,s,g)
        else:
            if res[2]==False:
                res =(ele,s,g)
            elif s==False and g==True:
                res =(ele,s,g)
    return res

def gentuple(n):
    if n%3==0:
        return zerotuples(n)
    elif n%3==1:
        return onetuples(n)
    else:
        return twotuples(n)

def genarray(array,p):
    res = []
    for ele in array:
        tupleset = gentuple(ele)
        res.append(choice(tupleset,p))
    g=0
    s=0
    for ele in res:
        if ele[2]==True:
            if ele[1]==True:
                s=s+1
                g=g+1
            else:
                g=g+1
    return (g,s)

def condans(array,p,s):
    anstuple = genarray(array,p)
    if anstuple[1]<=s:
        return anstuple[0]
    else:
        k=anstuple[1]-s
        return anstuple[0]-k
        
def main():
    ifile = open("C:\\B-large.in","r")
    ofile = open("C:\\outputl.txt","w")
    t=int(ifile.readline())
    i=1
    while i<=t:
        line = ifile.readline()
        line = line.split()
        n=line[0]
        s=int(line[1])
        p=int(line[2])
        array = []
        for ele in line[3:]:
            array.append(int(ele))
        ans = condans(array,p,s)
        ofile.write("Case #"+str(i)+": "+str(ans)+"\n")
        i=i+1
    ifile.close()
    ofile.close()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

    
