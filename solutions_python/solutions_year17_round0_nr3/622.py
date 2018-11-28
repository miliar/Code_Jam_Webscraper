fin = open("C-large.in","rt")

t = fin.readline().rstrip('\n')
t = int(t)

def insert(ls,x):
    for z in ls:
        if z[0] == x[0]:
            z[1] += x[1]
            return
    ls.append(x)
    ls.sort(key = lambda x: -x[0])
    return

def process(n,k):
    ints = [[n,1]]
    sInt = n
    while k > 0:
        tup = ints.pop(0)
        sInt = tup[0]
        k -= tup[1]

        k1 = (tup[0]-1)/2
        k2 = tup[0]-1-k1
        insert(ints,[k1,tup[1]])
        insert(ints,[k2,tup[1]])
        
    l1 = (sInt-1)/2
    l2 = sInt-1-l1
    tup = [max(l1,l2),min(l1,l2)]
    return " ".join([str(z) for z in tup])
        
fout = open("OUTPUT","wt")
for x in range(t):
    tup = fin.readline().rstrip('\n').split(" ")
    print tup,
    print ":",
    n = int(tup[0])
    k = int(tup[1])

    st = "Case #"+str(x+1)+": "
    st += process(n,k)
    print st
    fout.write(st+'\n')
    
fout.close()
