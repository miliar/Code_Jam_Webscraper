import sys

def ok(n):
    n = str(int(n))
    for i in xrange(1, len(n)):
        if int(n[i]) < int(n[i-1]):
            return False
    return True

def fix(n):
    flag = 0
    ret = ""
    n = str(int(n))

    for i in xrange(0, len(n)):
        if i == (len(n) - 1) and not flag:
            ret += n[i]

        elif flag == 1:
            ret += '9'

        elif int(n[i]) > int(n[i+1]):
            ret += str(int(n[i]) - 1)
            flag = 1

        else: ret += n[i]

    return ret

sys.stdin = open("B-largee.in", "r")
sys.stdout = open("B-largee.out", "w")

T = int(raw_input())

for t in xrange(T):
    n = raw_input()
    while not ok(n): n = fix(n)
    print "Case #%d: %d" % (t + 1, int(n))
