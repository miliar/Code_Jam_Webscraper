#!/usr/bin/python

def mkdir_count(existent, to_create):
    existent = [tuple(x.split('/')[1:]) for x in existent]
    to_create = [tuple(x.split('/')[1:]) for x in to_create]
    q = 0
    for full_path in to_create:
        current_path = ()
        for item in full_path:
            current_path += (item,)
            if current_path not in existent:
                existent.append(current_path)
                q += 1
    return q

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n, m = [int(s) for s in raw_input().split()]
        existent = []
        to_create = []
        for j in range(n):
            existent.append(raw_input())
        for j in range(m):
            to_create.append(raw_input())
        print 'Case #%d: %d' % (i+1, mkdir_count(existent, to_create))
