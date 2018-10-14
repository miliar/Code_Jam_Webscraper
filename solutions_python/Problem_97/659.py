table={1:0,2:36,3:801,4:12060,5:161982,6:2023578}

def presmetajistiorder(a,b,order):
    res = set([])
    for i in range(a,b+1):
        m = i
        for j in range(order): 
            last_digit = m%10
            m = last_digit*10**order + m/10
            if (last_digit==0) or (i>m): continue           
            if (i < m) and (m <=b):
                res.add((i,m))
    return len(res)

def presmetaj(a,b):
    ordera = len(str(a)) -1
    orderb = len(str(b)) -1
    if (ordera == orderb):
        return presmetajistiorder(a,b,ordera)
    res = presmetajistiorder(a,(10**(ordera+1))-1,ordera) + presmetajistiorder((10**(orderb)),b,orderb)
    for u in range(ordera+2,orderb+1):
        res += table[u]
    return res
    
def presmetajs(s):
    ns = [int(x) for x in s.split()]
    a = ns[0]
    b = ns[1]
    return presmetaj(a,b)

f = open('input', 'rU')
f2 = open('output', 'w')
r = ''
for i in range(int(f.readline())):
    r+='Case #' + str(i+1) + ': ' + str(presmetajs(f.readline())) + '\n'
f2.write(r)
f.close()
f2.close()