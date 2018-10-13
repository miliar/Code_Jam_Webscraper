from collections import deque

T = int(raw_input())


def conv(x):
    return bin(x)[2:].replace('1', '-').replace('0', '+')


def bfs(k, l, root):
    if root == 0:
        return 0
    q = deque()

    q.append((0, root))
    seen = {root}

    while len(q):
        d, s = q.popleft()
        mask = 2**k - 1

        for i in range(l - k + 1):
            x = s ^ mask
            #print("S: {}  M: {}  X: {}".format(conv(s), conv(mask), conv(x)))
            if x == 0:
                return d + 1
            elif x not in seen:
                q.append((d + 1, x))
                mask = mask << 1
                seen.add(x)
    return None

for t in range(T):
    line = raw_input()
    flips, K = line.split()

    K = int(K)
    root = 0
    for f in flips:
        root = root << 1
        if f == '-':
            root |= 1
    r = bfs(K, len(flips), root)
    if r is None:
        print("Case #{}: IMPOSSIBLE".format(t + 1))
    else:
        print("Case #{}: {}".format(t + 1, r))
