'''
Created on May 6, 2011

@author: ola
'''

gen = {}
badboys = []

def rep(ls):
    #print "in rep w",ls
    if len(ls) > 1:
        last = ''.join(ls[-2:])
        if last in gen:
            re = gen[last]
            ls = ls[:-2]+[re]
            #print "recurserep",ls
            return rep(ls)
        else:
            b0 = ls[-1]
            for x in ls[:-1]:
                check = b0+x
                if check in badboys:
                    return []
    return ls

def once(st):
    global gen, badboys
    #print "processing ",st
    ls = []
    for ch in st:
        ls.append(ch)
        ls = rep(ls)
    
    if len(ls) == 0:
        return "[]"
    ret = '['
    for ch in ls[:-1]:
        ret += ch+", "
    ret += ls[-1]+"]"
    return ret
        

def solve(n):
    global gen,badboys
    gen.clear()
    badboys = []
    data = raw_input().split()
    #print "read",data,n
    gc = int(data[0])
    curr = 1
    for x in range(gc):
        g = data[curr]
        curr += 1
        st = g[:2]
        gen[st] = g[2]
        st = g[1]+g[0]
        gen[st] = g[2]
    bc = int(data[curr])
    curr += 1
    for x in range(bc):
        g = data[curr]
        curr += 1
        badboys.append(g)
        g2 = g[1]+g[0]
        badboys.append(g2)
    st = data[curr+1]
    
    print "Case #%d: %s" % (n,once(st))

def main():
    t = int(raw_input())
    #print "# cases = ",t
    for x in xrange(t):
        solve(x+1)

if __name__ == "__main__":
    main()