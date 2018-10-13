from collections import deque


def flip_num(s, k):
    p = map(lambda x: x == "+", s)
    ans = 0
    d = deque()
    flipped = False
    for c in p:
        if not d:
            if not c:
                d = deque([False] * (k - 1))
                ans += 1
                flipped = True
        else:
            if (flipped != d.popleft()) == c:
                ans += 1
                if not d:
                    flipped = True
                    d = deque([False] * (k - 1))
                else:
                    d.extend((k - 1 - len(d)) * [flipped])
                    flipped = not flipped
    return "IMPOSSIBLE" if d else ans

if __name__ == "__main__":
    with open("input") as fi,\
            open("output", "w") as fo:
        t = int(fi.readline())
        for i in range(t):
            s, k = fi.readline().split()
            k = int(k)
            fo.write("Case #{}: {}\n".format(i + 1, flip_num(s, k)))
            #print("Case #{}: {}".format(i + 1, flip_num(s, k)))
