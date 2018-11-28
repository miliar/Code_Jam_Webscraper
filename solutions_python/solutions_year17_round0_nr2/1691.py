from __future__ import print_function
import sys

def gettidy(x):
    x = [0] + x
    index = 2
    while index < len(x) and x[index-1] <= x[index]:
        index += 1
    if index == len(x):
        return ''.join(map(str,x)).lstrip('0')
    index -= 1
    while x[index]-1 < x[index-1]:
        index -= 1
    x[index] = x[index] - 1
    for i in range(index+1, len(x)):
        x[i] = 9
    return ''.join(map(str,x)).lstrip('0')

if len(sys.argv) < 2:
    print("Missing input file name")
    quit()
with open(sys.argv[1], "r") as f:
    T = int(f.readline())
    data = []
    for x in range(T):
        N = [int(x) for x in list(f.readline().strip())]
        print("Case #%d: %s" % (x + 1, gettidy(N)))

