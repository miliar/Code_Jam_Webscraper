#!/usr/bin/python3

import sys

def main():
    with open(sys.argv[1]) as f:

        n_cases = int(f.readline())

        #print("Num cases: {}".format(n_cases))

        for _ in range(n_cases):
            p, n = f.readline().split(' ')
            n = int(n)
            ps = len(p)
            g = '+'*ps
            c = 0
            p = list(p)
            for i in range(ps-n+1):
                if p[i] is '-':
                    p[i:i+n] = flip( p[i:i+n] )
                    c += 1


            p = str.join('',p)
            #print(p)
            if p == g:
                print("Case #{}: {}".format(_+1,c))
            else:
                print("Case #{}: IMPOSSIBLE".format(_+1))


def flip(s):
    s = str.join('',s)
    s = s.replace('-','.')
    s = s.replace('+','-')
    s = s.replace('.','+')
    return list(s)



if __name__ == '__main__':
    main()
