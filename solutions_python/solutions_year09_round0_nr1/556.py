#!/usr/bin/python
# Google code jam 2009 

import sys
import re
aliandict = []
count = 0

def solve(tokens, val):
    global aliandict, count
    c = 0
    for a in aliandict:
        if a.startswith(val):
            c = 1
    if not c:
        return
    if len(tokens) == 0:
        if val in aliandict:
            #print val
            count = count + 1
        return

    for i in tokens[0]:
        solve(tokens[1:], val + i)

def main():
    global aliandict, count
    infile = file(sys.argv[1])
    lines = infile.readlines()
    (l, d, n) = lines[0].split(" ")
    l = int(l)
    d = int(d)
    n = int(n)
    aliandict = [x.strip() for x in lines[1:d+1]]
    #print aliandict, l, n
    for i in range(0, n):
        count = 0
        tokens = []
        test = lines[d+1+i].strip()
        token = 0
        bracket = 0
        #print test
        for j in test:
            if j == "(":
                bracket = 1
                continue
            if j == ")":
                bracket = 0
                token = token + 1
                continue
            try:
                tokens[token].append(j)
            except IndexError:
                tokens.append([j])
            if bracket == 0:
                token = token + 1
        #print tokens            
        solve(tokens, "")
        print "Case #%d: %d" % (i+1, count)
    

if __name__ == "__main__":
    main()
