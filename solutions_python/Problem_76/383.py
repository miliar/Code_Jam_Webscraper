#!/usr/bin/python

def solve():
    n = int(raw_input())
     
    l_n = map(int, raw_input().split(' '))
     
    reduction = reduce(lambda x,y: x ^ y, l_n)
    if reduction != 0:
        return "NO"
    
    l_n.sort()
    return sum(l_n[1:])
    

if __name__ == '__main__':
    T = int(raw_input())
    for case in range(1, T+1):
        print "Case #{0}: {1}".format(case, solve())
