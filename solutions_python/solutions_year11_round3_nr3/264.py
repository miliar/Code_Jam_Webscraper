#!/usr/bin/env python

def solves(n, freqs):
    if all(map(lambda a: a%n==0 or n%a==0 or a==1, freqs)):
        return True
    else:
        return False

def print_solution(freqs, n, l, h):
    for i in xrange(l, h+1):
        if solves(i, freqs):
            return str(i)
    
    return 'NO'

def main():
    T = int(raw_input())
    for i in xrange(T):
        n, l, h = map(int, raw_input().split(' '))
        freqs = map(int, raw_input().split(' '))
        print 'Case #{0}: {1}'.format(i+1, print_solution(freqs, n, l, h))

if __name__ == '__main__':
    main()
