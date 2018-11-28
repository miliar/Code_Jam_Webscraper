# -*- coding: utf-8
import time
def load_input():
    t = int(raw_input())
    q = []
    for i in xrange(int(t)):
        s, k = raw_input().split(' ')
        q.append({'l': init(s), 'k': int(k), 'N': len(s)})
    return (t, q)

def init(string):
    l = []
    for s in string:
        if s == '-':
            l.append(False)
        else:
            l.append(True)
    return l

def flip(l, i, k, N):
    if i+k > N:
        return []
    else:
        for j in xrange(i, i+k):
            l[j] = not(l[j])
        return l

def solve(l, k, N, t):
    c = 0
    for i in xrange(N-k+1):
        if not l[i]:
            flip(l, i, k, N)
            c += 1
    if all(l):
        print 'Case #%(t)d: %(c)d' % {'t':t, 'c':c}
    else:
        print 'Case #%(t)d: IMPOSSIBLE' % {'t':t}

def main():
    t, q = load_input()
    for i in xrange(t):
        solve(q[i]['l'], q[i]['k'], q[i]['N'], i+1)


if __name__ == '__main__':
    main()
