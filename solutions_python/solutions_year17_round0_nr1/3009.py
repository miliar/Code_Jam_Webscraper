import sys

sys.setrecursionlimit(1000000)

def flipper(s, k):

    def flipRange(s, startIndex, k):

        firstInv = -1

        for i in range(startIndex, startIndex + k):
            if s[i] == '+':
                s = s[:i] + '-' + s[i + 1:]
                if firstInv == -1:
                    firstInv = i
            else:
                s = s[:i] + '+' + s[i + 1:]

        return s, firstInv


    def uniform(s):

        return sum(map(lambda l : 0 if l == '+' else 1, s)) == 0


    def flipEval(s, k, invAt, accum):

        if uniform(s):
            return True, accum

        if invAt == -1:
            invAt = 0

        for i in range(invAt, len(s)):

            if s[i] == '-':
                if i + k > len(s):
                    return False, -1
                else:
                    flipped, invIndex = flipRange(s, i, k)
                    return flipEval(flipped, k, invIndex, accum + 1)

    return flipEval(s, k, -1, 0)

ret = []
with open('A-large.in', 'r') as file:
    t = int(file.readline())
    for _ in range(t):
        s, k = file.readline().split()
        k = int(k)

        outcome, flips = flipper(s, k)
        if not outcome:
            ret.append("IMPOSSIBLE")
        else:
            ret.append(str(flips))

with open('A_large-out.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s\n" % (i + 1, ret[i]))