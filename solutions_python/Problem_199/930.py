import sys
from collections import deque


def solve(caseNum, s, k):
    ans = query(s, k)
    print "Case #{}: {}".format(caseNum, ans if ans != None else "IMPOSSIBLE")

def flip(s):
    ans = ''
    for x in s:
        ans += '+' if x == '-' else '-'
    return ans

def query(s, k):
    n = len(s)
    queue = deque()
    queue.append((s, 0))
    visited = set()
    while queue:
        s, path = queue.popleft()
        visited.add(s)
        first_neg = s.find('-')
        if first_neg < 0: return path
        path += 1
        for i in range(first_neg, n-k+1):
            new_s = s[:first_neg] + flip(s[first_neg:first_neg+k]) + s[first_neg+k:]
            if not new_s in visited:
                queue.append((new_s, path))
    return None



t = int(input())  # read a line with a single integer

caseNum = 1
for line in sys.stdin:
    s, m = line.split(" ")  # read a list of integers, 2 in this case
    m = int(m)
    solve(caseNum, s, m)
    caseNum += 1
