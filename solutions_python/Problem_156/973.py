#!/usr/bin/env python3

# import heapq

# class MaxHeap(object):
#     def __init__(self, x):
#         self.heap = [-e for e in x]
#         heapq.heapify(self.heap)
#     def push(self, value):
#         heapq.heappush(self.heap, -value)
#     def pop(self):
#         return -heapq.heappop(self.heap)
#     def __str__(self):
#         return str([-v for v in self.heap])



def solve(pancakes):
    solutions = {}
    q = []
    m = max(pancakes)
    vec = [0] * (m+1)
    for p in pancakes:
        vec[p] += 1
    #pancakes.sort()
    q.append((0, vec))
    best = m
    while q:
        time, pancakes = q.pop()
        #print(">", time, pancakes)
        #v = pancakes.pop()
        v = len(pancakes)-1
        pancakes[v] -= 1
        if time+v < best:
            best = time+v
        if v > 3:
            for i in range(2, (v//2) + 1):
                pc = pancakes.copy()
                pc[v-i] += 1
                pc[i] += 1
                while pc and pc[-1] == 0:
                    pc.pop()
                q.append((time+1, pc))

    return best


testcases = int(input())

for case_n in range(1, testcases+1):
    input()
    case_data = list(map(int, input().split()))
    #print(case_data)
    #h = MaxHeap(case_data)
    #case_data = input().split()

    print("Case #%i: %s" % (case_n, solve(case_data)))