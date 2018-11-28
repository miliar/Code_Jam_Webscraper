#!/usr/bin/python
import sys
import collections


def input(filename):
    with open(filename) as f:
        lines = f.read().strip().split('\n')
        n = int(lines[0])
        assert n + 1 == len(lines)
        return [map(int, l.split()) for l in lines[1:n+1]]

def rotate(n):
    s = str(n)
    d = collections.deque(s)
    res = collections.deque() 
    for i in xrange(len(s)):
        d.rotate()
        res.append(int(''.join(d)))
    return tuple(res)
    
cache = {}
def rots(n):
    if n in cache:
        return cache[n]
    else:
        res = rotate(n)
        num_algarismos = len(str(n))
        for x in res:
            if len(str(x)) == num_algarismos:
                cache[x] = res
        return res

    
def answer(l):
    a, b = l
    pairs = set()
    for n in xrange(a, b):
        for m in rots(n):
            if n < m and m <= b:
                pairs.add((n,m))
    return len(pairs)


def process(filename):
    resp = [answer(l) for l in input(filename)]
    resp = zip(xrange(1,len(resp)+1), resp)
    return ['Case #%s: %s\n' % (i,r) for (i,r) in resp]

def do(inputfile, outputfile):
    with open(outputfile, 'w') as f:
        f.writelines(process(inputfile))

if __name__ == '__main__':
    inputfilename = sys.argv[1]
    do(inputfilename, '%s.output' % inputfilename)




    
