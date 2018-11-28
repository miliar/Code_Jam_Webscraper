import sys

def solve():
    line, num = sys.stdin.readline().strip().split()
    line = [True if i == '+' else False for i in line]
    num = int(num)
    
    flips = 0
    for i in range(0, len(line) - num + 1):
        if not line[i]:
            flips += 1
            for j in range(num):
                line[i + j] = not line[i + j]

    works = True
    for boolean in line:
        works = works and boolean

    if works:
        return flips
    
    return "IMPOSSIBLE"



t = int(sys.stdin.readline().strip())
for i in range(1, t+1):
    print("Case #%d: %s" % (i, str(solve())))
