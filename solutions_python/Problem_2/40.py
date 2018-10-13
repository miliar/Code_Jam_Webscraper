import sys

def readline():
    return sys.stdin.readline()

def normal_time(t):
    a, b = t.split(':')
    return int(a) * 60 + int(b)

def main():
    ncase = int(readline())
    for case in range(ncase):
        turntime = int(readline())
        na, nb = map(int, readline().split())

        q = []

        for i in range(na):
            f, t = map(normal_time, readline().split())
            q.append((f, 'start', 'a'))
            q.append((t+turntime, '0ready', 'b'))
        for i in range(nb):
            f, t = map(normal_time, readline().split())
            q.append((f, 'start', 'b'))
            q.append((t+turntime, '0ready', 'a'))

        q.sort()

        wait = { 'a': 0, 'b': 0 }
        need = { 'a': 0, 'b': 0 }
        for x in q:
            if x[1] == 'start':
                if wait[x[2]] == 0:
                    need[x[2]] += 1
                else:
                    wait[x[2]] -= 1
            if x[1] == '0ready':
                wait[x[2]] += 1
        print 'Case #%d: %d %d' % (case+1, need['a'], need['b'])




main()
