from sys import stdin

def rec(s):
    if len(s) == 1:
        return s
    if s[0] > s[1]:
        return chr(ord(s[0])-1) + '9' * (len(s) - 1)
    sub = rec(s[1:])
    if s[0] > sub[0]:
        return chr(ord(s[0])-1) + '9' * (len(s) - 1)
    return s[0] + sub

def main():
    t = int(stdin.readline().strip())
    for i in xrange(1, t+1):
        s = stdin.readline().strip()
        n = rec(s)
        if n[0] == '0':
            n = n[1:]
        print "Case #{}: {}".format(i, n)

main()
