from fractions import gcd

def mgcd(arr) :
    if len(arr) ==1 :
        return arr[0]
    
    r = None
    for i in range(0, len(arr)-1) :
        j, k = arr[i], arr[i+1]
        #print j, k
        l = gcd(j, k)
        
        if r == None :
            r = l
        else :
            r = gcd(r, l)
    return r

def process_case() :
    arr = map(int, raw_input().split())
    i = arr[0]
    arr = arr[1:]
    assert( len(arr) == i)
    
    arr.sort()
    diff = []
    
    for i in range(0, len(arr)-1) :
        j, k = arr[i], arr[i+1]
        diff.append(k-j)
    
    #print diff
    gg = mgcd(diff)
    toadd = arr[0] % gg
    if toadd != 0 :
        toadd = gg - toadd
    #print toadd
    return toadd

case_num = int(raw_input())
for i in range(case_num) :
    result = process_case()
    print "Case #%d: %s" % (i+1, result)