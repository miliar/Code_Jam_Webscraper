#!/usr/bin/env python3

def stall(n, k):
    stalls = [True] + [False for i in range(n)] + [True]
    lol, lel = 0, 0
    for ppl in range(k):
        max_lr, min_lr, best = -1, -1, -1
        l, r = 0, 0

        for i in range(n + 1):
            if stalls[i]:
                l = -1
                r = 0
                while not stalls[i + r + 1]:
                    r += 1
            else:
                l = l + 1
                r = r - 1
                # print('l {} r {}'.format(l, r))
                if min(l, r) > min_lr or (min(l, r) == min_lr and max(l, r) > max_lr):
                    max_lr = max(l, r)
                    min_lr = min(l, r)
                    best = i

        stalls[best] = True
        lol, lel = max_lr, min_lr
        # print(str(['+' if i else '-' for i in stalls]))

    return lol, lel

def main():
    cases = int(input())
    for c in range(1, cases + 1):
        [n, k] = [int(i) for i in input().split()]
        (max_lr, min_lr) = stall(n, k)
        print('Case #{}: {} {}'.format(c, max_lr, min_lr))

if __name__ == '__main__':
    main()
