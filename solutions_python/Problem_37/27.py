#!/usr/bin/env python

def digit(c, d):
    s = []
    n = c
    while n > 0:
        s.append(str(n % d))
        n = n / d
    return ''.join(reversed(s))

def solve(n, happy, unhappy):
    bases = map(lambda x: int(x), raw_input().split(' '))
    result = 2

    while True:
        inv = False
        for b in bases:
            if [result, b] in happy:
                continue
            dig = digit(result, b)
            mem = []
            
            while not inv:
                s = 0
                for d in dig:
                    s = s + int(d)**2
                    
                if s == 1:
                    break
                else:
                    if s in mem:
                        inv = True
                        break
                    else:
                        mem.append(s)
                        dig = digit(s, b)
            if inv:
                unhappy.append([result, b])
                break

        if not inv:
            for b in bases:
                happy.append([result, b])
            break
        
        result = result + 1
    
    print 'Case #%d: %d' % (n + 1, result)

def main():
    n = int(raw_input())
    happy = []
    unhappy = []
    for i in range(n):
        solve(i, happy, unhappy)

if __name__ == '__main__':
    main()

