#!/usr/bin/env python
import pprint as pp

def read():
    line = raw_input() 
    s = line.split()
    # data = [int(el) for el in s]
    return s


def run_test():
    data = read()

    sub = {}
    C = int(data[0])
    for c in xrange(C):
        word = data[c+1]
        sub.setdefault(word[0],{})[word[1]] = word[2]
        sub.setdefault(word[1],{})[word[0]] = word[2]

    opp = {}
    D = int(data[C+1])
    for d in xrange(D):
        word = data[d+C+2]
        opp.setdefault( word[0], set() ).add(word[1])
        opp.setdefault( word[1], set() ).add(word[0])
    
    res = []
    cnts = {}
    N = int(data[C+D+2])
    s = data[C+D+3]
    
    def add(x): 
        cnts[x] = 1+cnts.setdefault(x,0)
        res.append(x)

    def dec(x): 
        cnts[x] -= 1
        res.pop()

    for x in s:
        add(x)
        do = True
        #print
        #print "added", x
        #pp.pprint(res)
        #pp.pprint(cnts)
        while do:
            do = False
            z = res[-1]
            if len(res)>1 and z in sub:
                y = res[-2]
                if y in sub[z]:
                    dec(z)
                    dec(y)
                    add( sub[z][y] )
                    do = True
            if not do and z in opp:
                for y in opp[z]:
                    if y in cnts and cnts[y]>0:
                        res = []
                        cnts = {}
                        break

            #pp.pprint(res)
            #pp.pprint(cnts)


    return "[%s]"%(', '.join(res))
    

def main():
    tests = int(raw_input())
    for test in xrange(tests):
        print "Case #%i: %s"%(test+1, str(run_test()))

main();
