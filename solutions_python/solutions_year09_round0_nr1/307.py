#!/usr/bin/env python

def read_pattern(patstr):
    i = 0
    pattern = []
    while i < len(patstr):
        if patstr[i] != '(':
            pattern.append(set(patstr[i]))
            i += 1
        else:
            pos = patstr.find(')', i)
            pattern.append(set(patstr[i+1:pos]))
            i = pos+1
    return pattern

def solve_case(words, fin):
    pattern = read_pattern(fin.readline())
    match = 0
    for word in words:
        i = 0
        for pat in pattern:
            if word[i] not in pat:
                break;
            i += 1
        else:
            match += 1
    return match


def solve(fin):
    L, D, N = [int(i) for i in fin.readline().split(' ')]
    words = []
    for i in range(D):
        words.append(fin.readline())
    
    for i in range(N):
        out = solve_case(words, fin)
        print 'Case #{0}: {1}'.format(i+1, out)

def main():
    import sys
    solve(sys.stdin)

if __name__ == '__main__':
    main()
