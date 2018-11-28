from string import *

# convert a decimal (denary, base 10) integer to a binary string (base 2)
# tested with Python24 vegaseat 6/1/2005
 
ad2bin = {}
ab2dec = {}
aadd = {}

def d2bin(n):

    ini = n

    if ad2bin.has_key(n):
        return ad2bin[n]

    else:

        '''convert denary integer n to binary string bStr'''
        bStr = ''
        if n < 0: raise ValueError, "must be a positive integer"
        if n == 0: return '0'
        while n > 0:
            bStr = str(n % 2) + bStr
            n = n >> 1


    ad2bin[ini] = bStr
    return bStr
 
def b2dec(n):
    
    ini = n

    if ab2dec.has_key(n):
        return ab2dec[n]
    else:
        index = 0
        resp = 0
        while n >= 1:
            resp += (2**index) * (n%10)
            n /= 10
            index += 1
    
    ab2dec[ini] = resp

    return resp

def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def add(n,m):

    if aadd.has_key((n,m)):
        return aadd[(n,m)]
    elif aadd.has_key((m,n)):
        return aadd[(m,n)]
    else:

        bn = d2bin(n)
        bm = d2bin(m)
        lbn = len(bn)
        lbm = len(bm)
        br = ""

        minl = min(lbm,lbn)

        for x in range(minl):
   
            if bn[lbn -1 - x] == '0' and bm[lbm -1 - x] == '0':
                br = '0' + br
            if bn[lbn -1 - x] == '0' and bm[lbm -1 - x] == '1':
                br = '1' + br 
            if bn[lbn -1 - x] == '1' and bm[lbm -1 - x] == '0':
                br = '1' + br 
            if bn[lbn -1 - x] == '1' and bm[lbm -1 - x] == '1':
                br = '0' + br  

        if lbn == minl:
            br = bm[0:lbm-minl]+br
        else:
            br = bn[0:lbn-minl]+br


    aadd[(n,m)] = b2dec(int(br))
    return b2dec(int(br))

def solve(file):

    ab2dec.clear()
    ad2bin.clear()

    case = 0
    f = open("out_"+file,'w')

    inp = open(file)

    n = int(inp.readline())

    for x in range(n):
        num = int(inp.readline())
        items = split(inp.readline())
        maxn = -1
        comb = (2**(num))-1

        for i in range(comb-1):
            n = i+1
            nb = int2bin(n,num)
            rs0 = 0
            rs1 = 0
            fs0 = 0
            fs1 = 0
            
            for j in range(len(nb)):
                if nb[j] == '0':
                    rs0 += int(items[j])
                    fs0 = add(fs0,int(items[j]))
                else:
                    rs1 += int(items[j])
                    fs1 = add(fs1,int(items[j]))

            if fs1 == fs0:
                maxn = max(maxn,max(rs0,rs1))

        case += 1
        if maxn < 0:
            sol = "Case #"+str(case)+": NO"+'\n'
        else:
            sol = "Case #"+str(case)+": "+str(maxn)+'\n'
        
        print sol

        f.write(sol)

