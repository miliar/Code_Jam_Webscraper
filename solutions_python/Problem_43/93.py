#!/usr/bin/env python

def solve(message):
    count = 1
    lookup = {}
    base = len(set(message))
    if base == 1:
        base = 2
    for elem in message:
        if lookup.get(elem, None) is None:
            if count == 2 and len(lookup) == 1:
                lookup[elem] = 0
            else:
                lookup[elem] = count
                count += 1
    number = 0
    #print 'For input', message, 'base is', base
    #print lookup
    for i, elem in enumerate(reversed(message)):
        number += lookup[elem] * base**i
    return number

def main():
    T = int(raw_input())
    for count in range(T):
        message = raw_input()
        answer = solve(message)
        print 'Case #%d: %d' % (count + 1, answer)

if __name__ == '__main__':
    main()

