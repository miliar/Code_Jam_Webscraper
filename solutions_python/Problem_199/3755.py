import sys
sys.setrecursionlimit(1500)
def flip(a):
    if a == '-':
        return '+'
    return '-'

def func(s, fs):
    def infunc(b, c):
        #print b
        flag = True
        for i in b:
            if i == '-':
                flag = False
                break
        if flag:
            return c

        if len(b) < fs:
            return -1

        if b[0] == '-':
            for i in xrange(fs):
                b[i] = flip(b[i])
            c += 1
        return infunc(b[1:], c)

    c = infunc(s, 0)
    if c < 0:
        return "IMPOSSIBLE"
    return c

def main():
    s, fs = raw_input().split()
    return func(list(s), int(fs))

T = int(raw_input())
N = 1
while T:
    print "CASE #{}:".format(N), main()
    N += 1
    T -= 1
