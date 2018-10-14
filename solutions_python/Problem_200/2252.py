import sys
"""
import logging
level = logging.INFO
format = '  %(message)s'
handlers = [logging.FileHandler('filename.log'), logging.StreamHandler()]
logging.basicConfig(level = level, format = format, handlers = handlers)
"""

t =  int(input())

def solve(n):
    num = [int(d) for d in n]
    m = 9
    for i in range(len(n) - 1, -1, -1):
        if num[i] > m:
            num[i] -= 1
            for j in range(i + 1, len(n)):
                num[j] = 9
        m = num[i]
    s = ""
    for d in num:
        s += str(d)
    return int(s)

for i in range(1, t + 1):
    line = sys.stdin.readline().strip("\n")
    #Do stuff with the line
    solution = solve(line)
    print("Case #{}: {}".format(i, solution))
