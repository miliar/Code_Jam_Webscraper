def do_normal(n, ary_k, ary_n):
    cnt = n
    ind_k = [True]*n
    for i in xrange(n): 
        for j in xrange(n): 
            if ind_k[j]: 
                if ary_k[j] > ary_n[i]:
                    ind_k[j] = False 
                    cnt -= 1 
                    break 
    return cnt

def do_decimal(n, ary_k, ary_n):
    cnt = 0
    ind_k = [True]*n
    chk = 0 
    for i in xrange(n):
        if ary_n[i] > ary_k[chk]:
            cnt += 1
            chk += 1 
    return cnt

f = open("D-large.in")
#f = open("d.in")
t = int(f.readline())
for i in xrange(t):
    n = int(f.readline())
    ary_n = map(float,f.readline().split())
    ary_k = map(float,f.readline().split())
    ary_n.sort() 
    ary_k.sort() 
    print "Case #{}: {} {}".format(i+1,do_decimal(n, ary_k, ary_n),do_normal(n ,ary_k, ary_n)) 
    #print n
    #print ary_n
    #print ary_k
