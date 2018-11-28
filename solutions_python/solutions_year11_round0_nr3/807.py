#! /usr/bin/python
from sys import argv

def cry_baby(file_name):
    res = []
    fin = open(file_name)
    lines = fin.readlines()
    tcases = int(lines.pop(0))
    kase = 1
    while kase <= tcases:
        N = lines.pop(0).strip()
        c = map(int, lines.pop(0).split())
        from operator import xor
        if reduce(xor, c):
            res.append("NO")
        else:
            res.append(str(sum(c) - min(c)))
        kase += 1
    return res

def write_file(res):
    fin = open('oput.txt','w')
    i = 0
    for sol in res:
        i += 1
        fin.write("Case #%d: %s" %(i, sol))
        fin.write("\n")
    fin.close()

script, file_name = argv
res = cry_baby(file_name)
write_file(res)
