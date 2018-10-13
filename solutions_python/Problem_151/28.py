"""
Google Code Jam 2014 Round 2 Problem D

Author  : chaotic_iak
Language: Python 3.3.4
"""

class IOHandlerObject(object):
    source = "d.in"
    target = "d.out"
    sfile = None
    tfile = None

    def __init__(self):
        self.sfile = open(self.source, "a+")
        self.sfile.seek(0)
        self.tfile = open(self.target, "w+")

    def getInput(self, mode=2):
        # 0: String
        # 1: List of strings
        # 2: List of integers
        inputs = self.sfile.readline().strip()
        if mode == 0:
            return inputs
        if mode == 1:
            return inputs.split()
        if mode == 2:
            return [int(x) for x in inputs.split()]

    def writeOutput(self, s="\n"):
        if isinstance(s, list): s = " ".join(s)
        s = str(s)
        self.tfile.write(s)

IOHandler = IOHandlerObject()
g = IOHandler.getInput
w = IOHandler.writeOutput

############################## SOLUTION ##############################
import itertools

def trie_node_count(a):
    if a == []: return 0
    s = set()
    for q in a:
        for i in range(len(q)):
            s.add(q[:i+1])
    return len(s)+1

t = int(g(0))
for q in range(t):
    w("Case #" + str(q+1) + ": ")
    m,n = g()
    s = []
    for i in range(m):
        s.append(g(0))
    mx = 0
    ct = 0
    a = itertools.product(range(n), repeat=m)
    for i in a:
        b = []
        for j in range(n): b.append([])
        for j in range(m):
            b[i[j]].append(s[j])
        res = sum(trie_node_count(x) for x in b)
        if res == mx:
            ct += 1
        elif res > mx:
            mx = res
            ct = 1
    w(str(mx) + " " + str(ct))
    w()