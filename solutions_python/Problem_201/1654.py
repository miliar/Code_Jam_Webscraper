import math

def a (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        line = lines[t].split(" ")
        stack = [(c == "+") for c in line[0]]
        size = int(line[1])
        fout.write("Case #" + str(t) + ": " + str(flips(stack, size)) + "\n")
        print(t)

def flips(stack, size):
    print(stack)
    if False not in stack:
        return 0
    for i in range(len(stack)):
        if len(stack)-i < size:
            return "IMPOSSIBLE"
        if not stack[i]:
            next = flips(list([not b for b in stack[i+1:i+size]]) + list(stack[i+size:]), size)
            if next == "IMPOSSIBLE":
                return "IMPOSSIBLE"
            return next + 1



def b (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        last = int(lines[t])
        fout.write("Case #" + str(t) + ": " + str(tidy(last)) + "\n")
        print(t)

def tidy (last):
    laststr = str(last)
    print(laststr)
    for i in range(len(laststr)):
        if i == len(laststr)-1:
            return(laststr)
        if laststr[i] > laststr[i+1]:
            if i == 0:
                prev = []
            if i > 0:
                prev = list(laststr[:i])
            if laststr[i] == "1":
                newlast = prev+[0]+[9]*(len(laststr)-i-1)
            if laststr[i] > "1":
                newlast = prev+[str(int(laststr[i])-1)]+[9]*(len(laststr)-i-1)
            return tidy(int(''.join([str(c) for c in newlast])))

def c (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        line = lines[t].split()
        n = int(line[0])
        k = int(line[1])
        print("Case #" + str(t) + ":")
        (more, less) = stalls({n: 1},k)
        fout.write("Case #" + str(t) + ": " + str(more) + " " + str(less)+"\n")
        
def stalls(dists, k):
    print(dists, k)    
    most = max(dists)
    numof = dists.pop(most)
    split = (math.ceil((most-1)/2),math.floor((most-1)/2))
    if k <= numof:
        return split
    if split[0] == split[1]:
        newdists = dictadd(dists, split[0], numof * 2)
        return stalls(newdists,k-numof) 
    if split[0]>split[1]:
        newdists = dictadd(dists, split[0], numof)
        newdists = dictadd(newdists, split[1], numof)
        return stalls(newdists, k-numof)
        
def dictadd(d, key, num):
    if key in d:
        d[key] = d[key]+num
    if key not in d:
        d[key] = num
    return d

primes_db = {}

def isprime(n):
    if n <= 1:
        return False
    if n in primes_db:
        return primes_db[n]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            primes_db[n] = False, i
            return False, i
    primes_db[n] = True, ""
    return True, ""

def d (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        l1 = lines[t].split()
        k = int(l1[0])
        c = int(l1[1])
        s = int(l1[2])
        fout.write("Case #" + str(t) + ": ")
        print ("Case #" + str(t) + ":")
        fout.write(fractile(k,c,s))
        fout.write("\n")

def fractile(k,c,s):
    if s >= k:
        ts = [str(n*(k**(c-1)) + 1) for n in range(k)]
        print(ts)
        return " ".join(ts)
    return "IMPOSSIBLE"
