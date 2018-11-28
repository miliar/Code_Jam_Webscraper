#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
import sys

map = { " ": " " }

def mapping():
    makemap("yeq", "aoz")
    makemap("ejp mysljylc kd kxveddknmc re jsicpdrysi",
                "our language is impossible to understand")
    makemap("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                "there are twenty six factorial possibilities")
    makemap("de kr kd eoya kw aej tysr re ujdr lkgc jv",
                "so it is okay if you want to just give up")

    es = map.keys()
    ps = map.values()
    if len(es) < 26:
        print("Ambiguous")
        sys.exit(1)
    elif len(es) == 26:
        for letter in [chr(code) for code in range(ord("a"), ord("z") + 1)]:
            if not letter in es:
                key = letter
            if not letter in ps:
                val = letter
        map[key] = val

def solve(case):    
    result = ""
    for c in case:
        result += map[c]

    return result

def makemap(encrypted, plain):
    if len(encrypted) != len(plain):
        print("Length mismatch: ", encrypted, plain)
        return

    for i in range(len(encrypted)):
        e = encrypted[i]
        p = plain[i]
        if e in map and map[e] != p: 
            print("Contradiction: %s should be %s, but %s" % (e, map[e], p))
            sys.exit(1)
        map[e] = p

def readinput(file):
    with open(file, "r") as fd:
        T = int(fd.readline())
        cases = []
        for i in range(T):
            cases.append(fd.readline().rstrip())
    return cases

def output(file, results):
    with open(file, "w") as fd:
        for i, s in enumerate(results):
            line = "Case #%d: %s" % (i + 1, s)
            print(line) 
            fd.write("%s\n" % line)

# main
file = "A-small-attempt1.in"
cases = readinput(file)

mapping()
results = []
for case in cases:
    result = solve(case)
    results.append(result)

output(file + ".output", results)


        