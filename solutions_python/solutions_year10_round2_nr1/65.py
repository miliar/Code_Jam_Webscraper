#!/usr/bin/python
import os, sys


def appendToPathTree(pathTree, paths):
    creates = 0
    for p in paths:
        parts = p.split('/')
        # Don't include root dir
        parts = parts[1:]
        curPathTree = pathTree
        for i in range(len(parts)):
            if parts[i] in curPathTree:
                curPathTree = curPathTree[parts[i]]
            else:
                #print 'creating %s' % parts[i]
                creates += 1
                curPathTree[parts[i]] = {}
                curPathTree = curPathTree[parts[i]]
    return (pathTree, creates)

def analyzePaths(existingPaths, targetPaths):
    # Build up a tree of paths
    #if (len(existingPaths) == 0):
    #    # Have to create root dir
    #    toAdd = 1
    #    pathTree = {}
    #else:
    #    toAdd = 0
    #    pathTree = appendToPathTree({}, existingPaths)[0]
    pathTree = appendToPathTree({}, existingPaths)[0]
    return appendToPathTree(pathTree, targetPaths)[1]

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        (n, m) = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        existingPaths = []
        for i in range(n):
            existingPaths.append(fileLines[index][:-1])
            index += 1
        targetPaths = []
        for i in range(m):
            targetPaths.append(fileLines[index][:-1])
            index += 1
        #print caseStr
        answer = analyzePaths(existingPaths, targetPaths)
        print "Case #%d: %d" % (caseNum + 1, answer)

if __name__ == '__main__':
    main(sys.argv[1])
