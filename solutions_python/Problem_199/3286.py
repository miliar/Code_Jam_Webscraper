from fibonacci_heap_mod import *


def get_next(s, k):
    n = len(s)
    for i in range(0, n - k + 1):
        yield s[:i] + ''.join(['-' if c == '+' else '+' for c in s[i:i+k]]) + s[i+k:]

def heuristic(s):
    return sum([1 if c == '-' else 0 for c in s])

def a_star(s, k):
    open_set = Fibonacci_heap()
    closed_set = set()

    d = {}
    d[s] = 0
    index = {}
    index[s] = open_set.enqueue(s, 0)

    while open_set:
        s = open_set.dequeue_min().get_value()
        closed_set.add(s)
        if '-' not in s:
            return d[s]

        for v in get_next(s, k):
            if v not in closed_set:
                if v not in d:
                    d[v] = d[s] + 1
                    index[v] = open_set.enqueue(v, d[v] + heuristic(v))
                elif d[v] > d[s] + 1:
                    d[v] = d[s] + 1
                    open_set.decrease_key(index[v], d[v] + heuristic(v))

    return 'IMPOSSIBLE'


T = int(input())
for i in range(T):
    s, k = input().split()
    k = int(k)
    d = a_star(s, k)
    print('Case #'+ str(i+1) +': ' + str(d))
