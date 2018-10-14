#!/usr/bin/python

import sys, datetime

def solve(n, r, o, y, g, b, v):
    if v > y or o > b or g > r:
        return 'IMPOSSIBLE'
    if v + y == n:
        if v < y :
            return 'IMPOSSIBLE'
        return 'YV'*y
    if g + r == n:
        if g < r :
            return 'IMPOSSIBLE'
        return 'GR'*y
    if o + b == n:
        if o < b :
            return 'IMPOSSIBLE'
        return 'OB'*y
    y -= v
    b -= o
    r -= g
    if r > y + b or y > r + b or b > r + y:
        return 'IMPOSSIBLE'
    s = []
    if y >= max(r, b):
        s.append('Y')
        y -= 1
    elif b >= max(y, r):
        s.append('B')
        b -= 1
    else:
        s.append('R')
        r -= 1
    while y or b or r:
        if max(y, b, r) > 1:
            if s[-1] == 'B':
                if y >= r:
                    s.append('Y')
                    y -= 1
                else:
                    s.append('R')
                    r -= 1
            if s[-1] == 'R':
                if y >= b:
                    s.append('Y')
                    y -= 1
                else:
                    s.append('B')
                    b -= 1
            else:
                if b >= r:
                    s.append('B')
                    b -= 1
                else:
                    s.append('R')
                    r -= 1
        else:
            if y == b == r:
                if s[0] == 'R':
                    if s[-1] in 'RB':
                        s.extend(['Y','R','B'])
                    else:
                        s.extend(['R','Y','B'])
                elif s[0] == 'B':
                    if s[-1] in 'RB':
                        s.extend(['Y','B','R'])
                    else:
                        s.extend(['R','B','Y'])
                else:
                    if s[-1] in 'RY':
                        s.extend(['B','Y','R'])
                    else:
                        s.extend(['R','Y','B'])
            elif y == b == 1:
                if s[-1] == 'Y' or s[0] == 'B':
                    s.extend(['B','Y'])
                else:
                    s.extend(['Y','B'])
            elif y == r == 1:
                if s[-1] == 'Y' or s[0] == 'R':
                    s.extend(['R','Y'])
                else:
                    s.extend(['Y','R'])
            elif r == b == 1:
                if s[-1] == 'R' or s[0] == 'B':
                    s.extend(['B','R'])
                else:
                    s.extend(['R','B'])
            elif y == 1:
                s.append('Y')
            elif r == 1:
                s.append('R')
            else:
                s.append('B')
            break
    i = 0
    while i < len(s) and (v or o or g):
        if s[i] == 'Y' and v:
            s.insert(i, 'YV'*v)
            v = 0
            i += 2
        elif s[i] == 'R' and g:
            s.insert(i, 'RG')
            g = 0
            i += 2
        elif s[i] == 'B' and o:
            s.insert(i, 'BO')
            o = 0
            i += 2
        else:
            i += 1
    return ''.join(s)

def parse(input_file):
    n, r, o, y, g, b, v = map(int, input_file.readline().strip().split())
    return (n, r, o, y, g, b, v)

def main():
    start = datetime.datetime.now()
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], "w") if len(sys.argv) > 2 else None
    print "Writing to %s" % sys.argv[2] if output_file else "No output file"
    test_cases = int(input_file.readline().strip())
    print "Test cases:",test_cases
    print '-----------------'
    for tc in xrange(1, test_cases + 1):
        output = "Case #%d: %s" % (tc, solve(*parse(input_file)))
        print output
        if output_file:
            output_file.write(output + "\n")
    print '-----------------'
    print "Written to %s" % sys.argv[2] if output_file else "No output file"
    print 'Elapsed time: %s' % (datetime.datetime.now() - start)
    input_file.close()
    if output_file:
        output_file.close()

if __name__ == "__main__":
    main()
