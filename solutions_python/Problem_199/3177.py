#!/usr/bin/python

from sys import stdin

def flip(row, i, k):
    if (i+k-1 >= len(row) or i < 0):
        return None
    for j in range(i,i+k):
        if row[j] == "+":
            row[j] = "-"
        elif row[j] == "-":
            row[j] = "+"
    return row

def popnode(openbin):
    node = openbin[0]
    openbin = openbin[1:]
    return (node, openbin)

def popcosts(costs):
    cost = costs[0]
    costs = costs[1:]
    return (cost, costs)

def getchildren(node, k):
    children = []
    for i in (range(len(node)-k+1)):
        child = flip(node[:],i,k)
        children.append(child)
    return children
    
def search(start, k):
    end = ["+"]*len(row)
    if start == end:
        return str(0)
    openbin = [start]
    costs = [0]
    while openbin:
        node, openbin = popnode(openbin)
        cost, costs = popnode(costs)
        children = getchildren(node, k)
        #print "children"
        #print children
        #print "openbin"
        #print openbin
        for child in children:
            if child != end and child not in openbin:
               # print "OLA"
                openbin.append(child)
                costs.append(cost+1)
            if child == end:
                return str(cost+1)
        if cost > 100:
            return "IMPOSSIBLE"


nb_tc = int(stdin.readline())
for i in range(nb_tc):
    row, k = stdin.readline().split()
    row = list(row)
    k = int(k)

    result = search(row,k)
    print "Case #" + str(i+1) + ": " + result

