from string import rstrip
import sys

lines = map(rstrip, sys.stdin.readlines())

num = int(lines[0])

for n in range(num):
    shy = map(int, lines[n+1][2:])
    output = 0
    num_people = 0
    for p in range(len(shy)):
        if num_people < p:
            output += 1
            num_people += 1
        num_people += shy[p]
    print("Case #%i: %i" % (n+1, output))
