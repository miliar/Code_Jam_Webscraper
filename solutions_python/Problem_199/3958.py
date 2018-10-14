# -*- coding: utf-8 -*-
from collections import deque

def arr_to_int(x):
    return sum(2**i*b for i, b in enumerate(x))

def int_to_arr(x, length):
    a=list(bin(x)[2:])
    a.reverse()
    while(len(a)<length):
        a.append('0')
    for i in range(len(a)):
        a[i]=a[i]=='1'
    return a

def get_children(state, flipper_size):
    queue = []
    for i in range(len(state)-flipper_size+1):
        newState = state[:]
        for j in range(i,i+flipper_size):
            newState[j]=not newState[j]
        queue.append(arr_to_int(newState))
    return queue

def isDoneState(state):
        done=True
        for s in state:
            done = done&(s==True)
        return done;


def bfs(graph, start,length):
    visited = set()
    queue = [{"state":start,"cost":0}]

    while queue:
        node = queue.pop()
        if node["state"] not in visited:
            visited.add(node["state"])
            if isDoneState(int_to_arr(node["state"],length)):
                return node["cost"]
            for neighbor in graph[node["state"]]:
                if neighbor not in visited:
                    queue.insert(0,{"state":neighbor,"cost":node["cost"]+1})
    return "IMPOSSIBLE"

class Problem:
    
    def __init__(self, string, size):
        self.flipper_size = size
        self.state = []
        for c in string:
            self.state.append(c=="+")
            
        self.graph={}
        for i in range(2**len(self.state)):
            s=int_to_arr(i,len(self.state))
            self.graph[i]=get_children(s,self.flipper_size)
        
    
    def solve(self, maxDepth=10):
        return bfs(self.graph,arr_to_int(self.state),len(self.state))
    

cases = int(input())
for i in range(cases):
    string = input().split(" ")
    p = Problem(string[0],int(string[1]))
    solution = p.solve(10000)
    print("Case #"+str(i+1)+": "+str(solution))