#!/usr/bin/env python

def has_valid_bounds(field, n, m, min_value):
    for row in range(n):
        if field[row][0] == min_value:
            return True
    for col in range(m):
        if field[n-1][col] == min_value:
            return True
    return False

def check_equality(line):
    return len(set(line)) == 1

def check_field(field, n, m, min_value):
    if not has_valid_bounds(field, n, m, min_value):
        return False

    for row in xrange(n):
        for col in xrange(m):
            if field[row][col] == min_value:
                if not (check_equality(field[row]) or \
                        check_equality([field[x][col] for x in xrange(n)])):
                    return False
    return True

with open('input.in') as f:
    n = int(f.readline())
    i = 1
    for run in xrange(n):
        dims = f.readline().split(' ')
        n = int(dims[0])
        m = int(dims[1])
        field = []
        min_value = 101
        for row in xrange(n):
            row = [int(a) for a in f.readline().split(' ')]
            if min(row) < min_value:
                min_value = min(row)
            field.append(row)

        if min_value < 101:
            if check_field(field, n, m, min_value):
                print 'Case #%d: YES' % i
            else:
                print 'Case #%d: NO' % i
        else:
            print 'Case #%d: NO' % i
        i += 1
