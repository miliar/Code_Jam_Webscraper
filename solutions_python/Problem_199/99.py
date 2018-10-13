#!/usr/local/bin/python
import sys

def solve():
    line = sys.stdin.readline()
    pancakes, k = line.split()
    pancakes = [c == '+' for c in pancakes]
    k = int(k)

    case = 1
    answer = 0
    for i in range(len(pancakes)):
        if not pancakes[i]:
            if (i + k > len(pancakes)):
                answer = "IMPOSSIBLE"
                break
            for j in range(i, i + k):
                pancakes[j] = not pancakes[j]
            answer += 1
    return answer

cases = int(sys.stdin.readline())
for case in range(cases):
    print "Case #{}: {}".format(case+1, solve())
