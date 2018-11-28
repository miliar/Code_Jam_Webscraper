#!/usr/bin/env python3

if __name__ == '__main__':
    T = int(input())

    for t in range(1,T+1):
        shy_max, v = input().split()
        shy_max = int(shy_max)
        v = [int(x) for x in list(v)]

        standing = v[0]
        friends = 0

        for i in range(1, shy_max+1):
            if i > standing:
                friends += (i - standing)
                standing = i
            standing += v[i]

        print('Case #{}: {}'.format(t, friends))
