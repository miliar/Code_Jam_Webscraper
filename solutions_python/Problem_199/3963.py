#!/bin/python3
import re
import queue

t = int(input())
happy_matcher = re.compile('^\\++$')


def find_solution(s, k):
    known_patterns = set()
    if is_ok(s):
        return 0

    q = queue.Queue()
    for index in range(0, len(s) - k + 1):
        q.put((s, index, 0))

    while q.qsize() > 0:
        current = q.get()
        r = flip(current[0], k, current[1])
        if r in known_patterns:
            continue
        known_patterns.add(r)
        if is_ok(r):
            return current[2] + 1
        for index in range(0, len(r) - k + 1):
            q.put((r, index, current[2] + 1))
    return None


def flip(s, k, index):
    return s[0:index] + ''.join([
        '-' if x == '+' else '+' for x in s[index:index+k]
    ]) + s[index+k:]


def is_ok(s):
    return True if happy_matcher.match(s) else False


for i in range(1, t+1):
    parts = input().split(" ")
    s = parts[0]
    k = int(parts[1])
    solution = find_solution(s, k)
    if solution is None:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i, solution))
