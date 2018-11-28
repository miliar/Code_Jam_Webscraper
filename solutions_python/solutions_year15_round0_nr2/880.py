#!/usr/bin/python
import copy
import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('b.small.in')
sys.stdout = open('b.small.out', 'w')
class Solution:
    def __init__(self):
        self.rlt = None
    def solve(self, state, cursor, curr):
        if cursor == 0 or sum(state[1:]) == 0:
            self.rlt = min(curr, self.rlt) if self.rlt else curr
            return
        # print state,cursor,curr
        # eat
        old = copy.copy(state)
        old_curr = curr
        state = [0] + state[2:] + [0]
        while cursor > 0 and state[cursor] == 0:
            cursor -= 1
        self.solve(state, cursor, curr + 1)
        # move
        for i in range(9,1,-1):
            if old[i] > 0:
                for j in range(1,i):
                    state = copy.copy(old)
                    state[j] += state[i]
                    state[i-j] += state[i]
                    curr = old_curr + state[i]
                    state[i] = 0
                    cursor = 9
                    while cursor > 0 and state[cursor] == 0:
                        cursor -= 1
                    self.solve(state, cursor, curr)
                break
                #state[i/2] += 1
                #state[(i+1)/2] += 1
                #curr += 1
                #state[i] -= 1
                #cursor = 9
                #while cursor > 0 and state[cursor] == 0:
                #    cursor -= 1
                #self.solve(state, cursor, curr)
                #break
if __name__ == "__main__":
    T = int(raw_input())
    for k in range(1,T+1):
        D = int(raw_input())
        P = [int(item) for item in raw_input().split()]
        state = [0 for i in range(10)]
        for i in range(D):
            state[P[i]] += 1
        solution = Solution()
        solution.solve(state, 9, 0)
        print 'Case #%d: %d'%(k,solution.rlt)
