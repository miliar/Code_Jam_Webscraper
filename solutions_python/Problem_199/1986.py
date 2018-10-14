import queue
import pdb


def is_impossibru(p, k):
    for i in range(len(p) - k + 1):
        old = p[i]
        for j in range(i + 1, i + k):
            if p[j] == old:
                return False
            old = (old + 1) % 2
    return True


def go(p, k):
    Q = queue.Queue()
    Q_n = queue.Queue()
    seen = set()
    Q_n.put(p)
    seen.add(tuple(p))
    l = 0
    while not Q_n.empty():
        l += 1
        # Copy Q_n to Q
        while not Q_n.empty():
            Q.put(Q_n.get())
        while not Q.empty():
            e = Q.get()
            for i in range(len(e)):
                if e[i] == 0:
                    start = max(0, i - k + 1)
                    end = min(len(e) - 1, i + k - 1)
                    for j in range(start, end - k + 2):
                        n = e[:]
                        for s in range(j, j + k):
                            n[s] = (n[s] + 1) % 2
                        if len(n) == sum(n):
                            return l
                        tn = tuple(n)
                        if tn not in seen:
                            seen.add(tn)
                            Q_n.put(n)
    return 'IMPOSSIBLE'


def r():
    t = int(input())
    for i in range(1, t + 1):
        pancakes, k = input().split(" ")
        k = int(k)
        pancakes = [0 if x == '-' else 1 for x in pancakes]
        res = 'IMPOSSIBLE'
        # if not is_impossibru(pancakes, k):
        if len(pancakes) - sum(pancakes) == 0:
            res = 0
        else:
            res = go(pancakes, k)
        print('Case #' + str(i) + ':', str(res))

r()


