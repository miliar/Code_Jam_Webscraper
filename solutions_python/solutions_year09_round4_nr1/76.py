#!/usr/bin/env python

def solve(n):
    count = 0
    mat = []
    rows = int(raw_input())
    for row in range(rows):
        line = reversed(raw_input())
        t = []
        for l in line:
            t.append(l)
        mat.append(''.join(t))

    for i in range(rows):
        token = list('0'*rows)
        for j in range(rows-i-1, rows):
            token[j] = '1'
        pivot = ''.join(token)
        if mat[i] > pivot:
            for j in range(i+1, rows):
                if mat[j] <= pivot:
                    for k in range(j, i, -1):
                        mat[k], mat[k-1] = mat[k-1], mat[k]
                        count += 1
                    break
    
    print 'Case #%d: %d' % (n+1, count)

def main():
    cases = int(raw_input())
    for case in range(cases):
        solve(case)

if __name__ == '__main__':
    main()
