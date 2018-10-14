def change(s, l, r):
    for i in xrange(l, r):
        if s[i] == '-':
            s[i] = '+'
        else:
            s[i] = '-'


def solve(s, k):
    counter = 0
    for i in xrange(len(s)):
        if s[i] == '-' and i < len(s) - k + 1:
            counter += 1
            change(s, i, i + k)
    return counter


def main():
    n = input()
    for i in xrange(n):
        inp = raw_input()
        s = list(inp.split()[0])
        k = int(inp.split()[1])
        res = solve(s, k)
        if "".join(s) == len(s) * '+':
            print "Case #" + str(i + 1) + ": " + str(res)
        else:
            print "Case #" + str(i + 1) + ": " + "IMPOSSIBLE"

main()