#!/usr/bin/python

import sys, math

class Node:
    def __init__(self, b=0, c=0, v=0, p=None):
        self.bool = b
        self.val = v
        self.change = c
        self.children = []
        if p: p.addChild(self)
        self.parent = p
    def addChild(self, c):
        self.children.append(c)

def getVal(t):
    if not(t.children): return t.val
    else:
        if t.bool == 1:
            return t.children[0] and t.children[1]
        else:
            return t.children[0] or t.children[1]

def makeVal(tree, V):
    if getVal(tree) == V: return 0
    if not tree.children: return "IMPOSSIBLE"
    if V == 1:
        a = makeVal(tree.children[0],1)
        b = makeVal(tree.children[1],1)
        if tree.bool == 1:
            if tree.change:
                if a == "IMPOSSIBLE":
                    if b == "IMPOSSIBLE":
                        return "IMPOSSIBLE"
                    else:
                        return 1 + b
                else:
                    if b == "IMPOSSIBLE":
                        return 1 + a
                    else:
                        return min(a+b, 1 + a, 1+b)
            else:
                if a == "IMPOSSIBLE": return "IMPOSSIBLE"
                if b == "IMPOSSIBLE": return "IMPOSSIBLE"
                return a + b
        else:
            if a == "IMPOSSIBLE": return b
            if b == "IMPOSSIBLE": return a
            return min(a,b)
    else:
        a = makeVal(tree.children[0],0)
        b = makeVal(tree.children[1],0)
        if tree.bool == 0:
            if tree.change:
                if a == "IMPOSSIBLE": 
                    if b == "IMPOSSIBLE": return "IMPOSSIBLE"
                    else: return 1 + b
                else:
                    if b == "IMPOSSIBLE": return 1 + a
                    else: return min(a+b, a+b, 1+a)
            else:
                if a == "IMPOSSIBLE": return "IMPOSSIBLE"
                if b == "IMPOSSIBLE": return "IMPOSSIBLE"
                return a+b
        else:
            if a == "IMPOSSIBLE": return b
            if b == "IMPOSSIBLE": return a
            return min(a,b)
    
def main( root, V ):
    ## Does the root have the value of its children?
    return makeVal(root, V)

def getline(fpin, types):
    args = fpin.readline().strip().split()
    for i in range(len(types)):
        args[i] = types[i](args[i])
    return args

def getall(fpin, type):
    return [type(x) for x in fpin.readline().strip().split()]

if __name__=="__main__":
    fpin=open(sys.argv[1])
    if len(sys.argv) > 2:
        fpout = open(sys.argv[2], 'w')
    else:
        fpout = sys.stdout


    cases = int(fpin.readline().strip())
    for case in range(1,cases+1):
        (M,V) = getall(fpin, int)
        nodeQueue = []
        for m in range((M-1)/2):
            G, C = getall(fpin, int)
            if nodeQueue:
                p = nodeQueue[0]
                if p.children: nodeQueue = nodeQueue[1:]
                nodeQueue.append(Node(b=G, c=C, p = p))
            else:
                root = Node(b=G, c=C)
                nodeQueue.append(root)
        for m in range((M-1)/2, M):
            v = getall(fpin, int)[0]
            p = nodeQueue[0]
            if p.children: nodeQueue = nodeQueue[1:]
            nodeQueue.append(Node(v=v, p = p))

        fpout.write("Case #%d: %s\n" % (case, main( root, V ) ))

