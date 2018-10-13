#!/usr/bin/python3

import sys

def main():
    with open(sys.argv[1]) as f:

        n_cases = int(f.readline())


        for _ in range(n_cases):
            d, n = f.readline().split(' ')
            n = int(n)
            d = int(d)

            t = []
            for __ in range(n):
                k, s = f.readline().split(' ')
                k = int(k)
                s = int(s)
                t.append((d - k)/s)

            tmax = max(t)
            smax = d/tmax

            print("Case #{}: {}".format(_+1,smax))


if __name__ == '__main__':
    main()
