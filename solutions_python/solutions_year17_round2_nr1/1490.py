from collections import deque

def compute(d, horses):
    max_t = 0
    for p, s in horses:
        new_t = (d-p)/s
        max_t = max(new_t, max_t)
    return d/max_t

# Process input
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        d, n = [int(l) for l in input().split()]
        horses = []
        for j in range(n):
            p, s = [int(k) for k in input().split()]
            horses.append((p, s))
        res = compute(d, horses)
        print("Case #{}: {}".format(i+1, res))
