#!/usr/bin/python

def isrecyc(a, b):
    if a >= b:
        return False
    astr = str(a)
    bstr = str(b)
    for i in range(1,len(astr)):
        tmp = bstr[i:] + bstr[:i]
        if tmp[0] == '0': 
            continue
        if tmp == astr:
            return True
    return False
    
def recyccount(a, minn, maxn):
    ret = 0
    astr = str(a)
    seen = {}
    for i in range(1,len(astr)):
        tmp = astr[i:] + astr[:i]
        if tmp[0] == '0': 
            continue
        tmpi = int(tmp)
        if minn <= tmpi <= maxn and not tmp in seen:
            # print a, tmpi, isrecyc(a, tmpi), not key in mapc
            seen[tmp] = ''
            ret += 1 
    return ret
     
def recyc(a, b):
    #nd = 0
    #ad = a
    #maxn = 0
    #while ad != 0:
    #    ad /= 10
    #    nd += 1
    #    maxn = maxn * 10 + 9
    #print "nd, maxn: ",  nd, maxn
    ret = 0 
    for i in range(a, b+1):
        ret += recyccount(i, i+1, b)
    return ret

def main():
    f=open('p2.i', 'r')
    f2=open('p2.o', 'w')
    i = 0
    for line in f:
        if i == 0:
            nt = int(line)
        else:
            ns = line.split()
            A = int(ns[0])
            B = int(ns[1]) 
            print A, B
            f2.write("Case #%d: %d\n" % (i, recyc(A, B)))
        i += 1

if __name__ == "__main__":
    main()
