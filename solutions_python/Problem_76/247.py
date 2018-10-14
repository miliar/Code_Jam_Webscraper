#!/usr/bin/env python
# encoding: utf-8

def existe_sol(l):
    return (xorear(l) == 0)

def xorear(l):
    result = 0
    for i in l:
        result = result^i
    return result

def parse_input(fileDescriptor):
    f = fileDescriptor

    n = int(f.readline())
    listOfints = map(lambda x: int(x),f.readline().split(' '))

    return listOfints

def ser_hermano_malo(l):
    return sum(l) - min(l)

def solve(filename):
    f = open(filename, "r")
    fsol = open("solucion.txt", "w")

    t = int(f.readline())
    for i in xrange(t):
        l = parse_input(f)
        if not existe_sol(l):
            r = "NO"
        else:
            r = str(ser_hermano_malo(l))
        fsol.write("Case #%d: %s\n" %(i+1, r))
