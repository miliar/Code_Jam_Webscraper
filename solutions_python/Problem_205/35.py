#!/usr/bin/python3
import itertools
from heapq import heappush, heappop
import math
import pprint

#def pathTo(node, cameFrom):
#    path = [node]
#    while node in cameFrom:
#        node = cameFrom[node]
#        path.append(node)
#    return list(reversed(path))

def search(start):
    counter = itertools.count()
    closed = set()
    queue = [(start.heuristic(), next(counter), start)]
    bestCostTo = {start: 0}
    cameFrom = {}

    while len(queue) > 0:
        _, _, node = heappop(queue)

        if node.isGoal():
#            print(pathTo(node,cameFrom))
            return bestCostTo[node], node
        closed.add(node)

        for edgeCost, nextNode in node.neighbors():
            if nextNode in closed:
                continue
            if nextNode.isFailure():
                continue

            nextCost = bestCostTo[node] + edgeCost
            if nextCost >= bestCostTo.get(nextNode, float('inf')):
                continue

#            cameFrom[nextNode] = node
            bestCostTo[nextNode] = nextCost
            heappush(queue, 
                    (nextCost + nextNode.heuristic(), next(counter), nextNode))

    return "failure", tuple()


class Node:
    def __init__(self, dHP, kHP, dA, kA, win, dead):
        self.dHP = dHP
        self.kHP = kHP
        self.dA = dA
        self.kA = kA
        self.win = win
        self.dead = dead

    def isGoal(self):
        return self.win

    def isFailure(self):
        return self.dead and not self.win

    def neighbors(self):
        if not self.isGoal() and not self.isFailure():
            yield     (1,Node(self.dHP - self.kA,           self.kHP - self.dA, self.dA,    self.kA,            self.kHP - self.dA <= 0,self.dHP - self.kA <= 0))
            if B > 0:
                yield (1,Node(self.dHP - self.kA,           self.kHP,           self.dA + B,self.kA,            self.kHP <= 0,          self.dHP - self.kA <= 0))
            yield     (1,Node(Hd - self.kA,                 self.kHP,           self.dA,    self.kA,            self.kHP <= 0,          Hd - self.kA <= 0))
            if D > 0:
                yield (1,Node(self.dHP - max(self.kA - D,0),self.kHP,           self.dA,    max(self.kA - D,0), self.kHP <= 0,          self.dHP - max(self.kA - D,0) <= 0))

    def heuristic(self):
        return 0

    def key(self):
        return (self.dHP, self.kHP, self.dA, self.kA, self.win, self.dead)

    def __eq__(self, other):
        return isinstance(other, Node) and self.key() == other.key()

    def __hash__(self):
        return hash(self.key())

    def __repr__(self):
        return repr(self.key())

T = int(input())
for t in range(1, T+1):
    Hd, Ad, Hk, Ak, B, D = (int(i) for i in input().strip().split())
    start = Node(Hd, Hk, Ad, Ak, False, False)
    cost, state = search(start);
    if cost == "failure":
        print("Case #%d: IMPOSSIBLE" % t)
    else:
        print("Case #%d: %d" % (t, cost))
