#! /usr/bin/env python

def solve() :
    N = int(raw_input())
    a = [int(x) for x in raw_input().split()]
    
    x = reduce((lambda s, t: s ^ t) , a)
    if x != 0: 
        return "NO"
    else:
        return sum(a) - min(a)

def main() :
    T = int(raw_input())
    for tno in range(T):
        res = solve()
        print "Case #" + str(tno + 1)+ ": " + str(res)

if __name__ == '__main__':
    main()
