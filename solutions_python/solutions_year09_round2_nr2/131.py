#!/usr/bin/env python
import sys,math,psyco

def calc(ns):
    ns = map(int, [x for x in ns])
    C=ns[:]
    #print ns
    ii=-1
    for i in range(len(ns)-1):
        if ns[i]<ns[i+1]: 
            ii=i

    #print ii
    if ii==-1: 
        ns.sort()
        if ns[0]==0:
            for i,n in enumerate(ns):
                if n == 0: continue
                ns[0], ns[i] = ns[i], ns[0]
                break
            ns.insert(1,0)
        else:
            ns.insert(1,0)

    else:
        rs = []
        #for i in range(ii)+[len(ns)-1]+range(ii, len(ns)-1):
        #    rs.append(ns[i])

        #ns = rs

        s = ns[ii+1:]
        s.sort()
        t = None
        for j in range(len(s)): 
            if s[j] > ns[ii]: 
                #rs += s[j]
                t = s[j]
                break
        #first = True
        #for i,n in enumerate(ns):
        #    if i < ii: 
        #        rs.append(n)
        #        continue
        #    if i == ii:
        #        rs.append(s[j])
        #        continue
        #    if n==s[j] and first:
        #        ns[i] = ns[ii]
        #        rs.append(ns[ii])
        #        break
        #    else:
        #        rs.append(n)
        #        #first = False
        #    
        #    #if not first: break

        #k = ns[i+1:]
        #k.sort()
        #rs += k
        for j in range(ii,len(ns)):
            if ns[j] == t:
                ns[ii], ns[j] = ns[j], ns[ii]
        #print ns
        k = ns[ii+1:]
        k.sort()
        rs = ns[:ii+1] + k

        ns = rs

    return "".join( str(s) for s in ns )

def main():
    N=0
    for nr,line in enumerate(sys.stdin):
        if nr==0:
            N=int(nr)
            continue
        print "Case #%d: %s" % (nr, calc(line.strip()))

if __name__ == "__main__": 
    psyco.full()
    main()
