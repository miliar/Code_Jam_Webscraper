#!/usr/bin/python

import sys

def solve(data):

    where = {'O': 1, 'B': 1}
    when = {'O': 0, 'B': 0}

    sol = 0

    for entry in data:
        bot, button = entry
        
        dist = abs(button-where[bot])
        time = sol-when[bot]

        sol += max(0, dist-time)+1

        where[bot] = button
        when[bot] = sol

    return sol

def main():
    t = int(sys.stdin.readline())

    for i in range(t):
        data = sys.stdin.readline().strip().split()[1:]
        
        data = zip(filter(lambda x : x in ['O', 'B'], data), 
                   map(int, filter(lambda x : x not in ['O', 'B'], data)))

        print 'Case #%d: %d' % (i+1, solve(data))

if __name__ == '__main__':
    main()
