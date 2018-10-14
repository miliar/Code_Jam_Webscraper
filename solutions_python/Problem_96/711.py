#!/usr/bin/python

def input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
        n = int(lines[0])
        return [map(int, l.split()) for l in lines[1:n+1]]

def span(x):
    q = x / 3
    r = x % 3
    if r == 2:
        return q + 1, q + 2
    elif r == 0:
        return q,     q + 1
    elif r == 1:
        return q + 1, q + 1

    
def answer(l):
    n, s, p = l[0:3]
    totais = l[3:]
    assert len(totais) == n
    tops, surprises = 0, s
    for t in totais:
        min, max = span(t)
        if min >= p:
            tops += 1
        elif max > min and max >= p and surprises > 0 and t > 0:
            tops += 1
            surprises -= 1
    return tops

def process(filename):
    resp = [answer(l) for l in input(filename)]
    resp = zip(xrange(1,len(resp)+1), resp)
    return ['Case #%s: %s\n' % (i,r) for (i,r) in resp]

def do(inputfile, outputfile):
    with open(outputfile, 'w') as f:
        f.writelines(process(inputfile))


import sys

if __name__ == '__main__':
    inputfilename = sys.argv[1]
    do(inputfilename, '%s.output' % inputfilename)




    
