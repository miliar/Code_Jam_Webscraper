#!/usr/bin/python3

import sys

def main():
    with open(sys.argv[1]) as f:

        n_cases = int(f.readline())

        #print("Num cases: {}".format(n_cases))

        rstore = []
        for _ in range(n_cases):
            n = int(f.readline())

            c = tidyup(n)

            print("Case #{}: {}".format(_+1,c))

def tidyup(n):
    ns = list(map(int, list(str(n))))

    for idx in range(len(ns)-1, 0, -1):
        if any([ns[idx] < nn for nn in ns[:idx]]):
            for ii in range(idx, len(ns)):
                ns[ii] = 9
            if idx is not 0:
                if ns[idx-1] is not 0: ns[idx-1] -= 1

    return int(str.join('',map(str, ns)))
                                                
    
def istidy(n):
    ns = map(int, list(str(n)))
    m = 1
    for nn in ns:
        if nn < m:
            return False
        else:
            m = max(m, nn)

    return True


if __name__ == '__main__':
    main()
