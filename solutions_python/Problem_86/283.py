import math

def is_prime(n):
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    i = 5
    w = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def prime_factors(num):
    pfactorsdict = {}
    pfactorslist = []
    while True:
        j = 2
        while j < num+1:
            if num%j==0 and is_prime(j):
                num = num/j
                pfactorsdict[j] = pfactorsdict.get(j,0) + 1
                pfactorslist.append(j)
                break
            j+=1
        if num==1:
            break
    return pfactorsdict

    
def dividees(num, L, H):
    pfs = prime_factors(num)
    factors = {}
    all = []
    for pf in pfs:
        factors[pf] = []
        for pow in range(pfs[pf]+1):
            candidate = pf**pow
            if candidate > H:
                continue
            factors[pf].append(candidate)
        all.append(factors[pf])

    all_small_enough = reduce(lambda x,y:  set(a*b for a in x for b in y if (a*b <= H)), all, set([1]))
    all_dividees = set(x for x in all_small_enough if (x>=L))
    #print "dividees of", num, all_dividees 
    return(all_dividees)

    
def multiples(num, L, H):
    lowtimes = int(math.ceil(float(L)/num))
    hightimes = int(math.floor(float(H)/num))
    all_multiples = map(lambda x: num*x, range(lowtimes, hightimes+1))
    #print "multiples of", num, all_multiples
    return(set(all_multiples))

    
def harmony(filename):
    f = open(filename, "r")
    T = int(f.readline())
    fo = open(filename+".out", "w")
    for t in range(0,T):
        (N, L, H) = map(lambda x: int(x), f.readline().split())
        notes = map(lambda x: int(x), f.readline().split())
        #print N, L, H
        #print notes
        smallest = dividees(min(notes), L, H).union(multiples(min(notes), L, H))
        possible_notes = reduce(lambda x,y: x.intersection(dividees(y, L, H).union(multiples(y, L, H))), notes, smallest)
        #print "smallest", smallest
        #print "possible", possible_notes
        if len(possible_notes)==0:
            fo.write("Case #"+str(t+1)+": NO\n")
        else:
            fo.write("Case #"+str(t+1)+": "+str(min(possible_notes))+"\n")
            
        #print 50*"-"
    fo.close()
    f.close()
