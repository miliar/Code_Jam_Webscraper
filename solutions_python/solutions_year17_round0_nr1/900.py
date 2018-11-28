import os
import sys

def update(s, i):
    if s[i] == "+":
        s[i] = "-"
    elif s[i] == "-":
        s[i] = "+"

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    for case in range(num):
        input = sys.stdin.readline().strip()
        s = [i for i in input.split(" ")[0]]
        num = int(input.split(" ")[1])

        move = 0
        for i in range(len(s)):
            if s[i] == "-":
                if i < len(s) - num + 1:
                    for j in range(num):
                        update(s, i+j)
                    move += 1
                else:
                    move = -1

        if move != -1:
            print "Case #%s: %s" % (case + 1, move)
        else:
            print "Case #%s: IMPOSSIBLE" % (case + 1)
