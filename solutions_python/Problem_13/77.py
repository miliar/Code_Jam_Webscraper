#!/usr/bin/python
import sys

AND = 1
OR  = 0
CHANGE = 1
NOCHANGE = 0

def isPossible(target,tree,root):
    values = {}
    for i in range(1,len(tree)+1):
        n = len(tree) - i + 1
        values[n] = {}
        node = tree[n]
        if len(node) == 1: # We have a leaf
            if node[0] == 0:
                values[n][0] = True,0
                values[n][1] = False,0
            else:
                values[n][0] = False,0
                values[n][1] = True,0
        else: # We have a gate
            if node[1] == NOCHANGE:
                if node[0] == AND:
                    values[n][1] = values[2*n][1][0] and values[2*n+1][1][0],values[2*n][1][1] + values[2*n+1][1][1]
                    values[n][0] = values[2*n][0][0] or values[2*n+1][0][0],min(values[2*n][0][1],values[2*n+1][0][1])
                else: # OR
                    values[n][0] = values[2*n][0][0] and values[2*n+1][0][0],values[2*n][0][1] + values[2*n+1][0][1]
                    values[n][1] = values[2*n][1][0] or values[2*n+1][1][0],min(values[2*n][1][1],values[2*n+1][1][1])
            else: # We have a mutable gate
                if node[0] == AND:
                    to1 = ([values[2*n][1][1] + values[2*n+1][1][1]] if values[2*n][1][0] and values[2*n+1][1][0] else []) + ([values[2*n][1][1] + values[2*n+1][0][1] + 1] if values[2*n][1][0] and values[2*n+1][0][0] else []) + ([values[2*n][0][1] + values[2*n+1][1][1] + 1] if values[2*n][0][0] and values[2*n+1][1][0] else [])
                    if to1 == []:
                        to1 = [1]
                    values[n][1] = values[2*n][1][0] or values[2*n+1][1][0],min(to1)
                    to0 = ([values[2*n][0][1]] if values[2*n][0][0] else []) + ([values[2*n+1][0][1]] if values[2*n+1][0][0] else [])
                    if to0 == []:
                        to0 = [1]
                    values[n][0] = values[2*n][0][0] or values[2*n+1][0][0],min(to0)
                else: # OR
                    to0 = ([values[2*n][0][1] + values[2*n+1][0][1]] if values[2*n][0][0] and values[2*n+1][0][0] else []) + ([values[2*n][1][1] + values[2*n+1][0][1] + 1] if values[2*n][1][0] and values[2*n+1][0][0] else []) + ([values[2*n][0][1] + values[2*n+1][1][1] + 1] if values[2*n][0][0] and values[2*n+1][1][0] else [])
                    if to0 == []:
                        to0 = [1]
                    to1 = ([values[2*n][1][1]] if values[2*n][1][0] else []) + ([values[2*n+1][1][1]] if values[2*n+1][1][0] else [])
                    if to1 == []:
                        to1 = [1]
                    values[n][1] = values[2*n][1][0] or values[2*n+1][1][0],min(to1)
                    values[n][0] = values[2*n][0][0] or values[2*n+1][0][0],min(to0)
    return values[root][target]

def buildTree(tree,leaves):
    trees = {}
    for i in range(0,len(leaves)):
        trees[i+len(tree)+1] = (leaves[i],)
    for i in range(0,len(tree)):
        n = len(tree) - i
        trees[n] = tree[n - 1]
    return trees
    
if __name__ == '__main__':
    next = sys.stdin.readline
    numberOfCases = int(next())
    for caseNumber in range(1,numberOfCases+1):
        tree = []
        leaves = []
        # Process a case
        M,V = map(int,next().split())
        for i in range(1,(M-1) / 2 + 1):
            G,C = map(int,next().split())
            tree.append((G,C))
        for i in range(1,(M+1)/2 + 1):
            I = int(next())
            leaves.append(I)
        tree = buildTree(tree,leaves)
        possible,minimum = isPossible(V,tree,1)
        print "Case #" + str(caseNumber) + ": " + ('IMPOSSIBLE' if (not possible) else str(minimum))
