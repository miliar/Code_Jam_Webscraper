__author__ = 'phani'

import sys
import math

def print_matrix(matrix):
    output = ""
    for r in matrix:
        for x in r:
            output += x
        output += "\n"
    return output

def get_column_matrix(r, m):
    matrix = ["." for _ in xrange(r)]
    for i in xrange(m):
        matrix[i] = "*"
    matrix[-1] = "c"
    return matrix

def get_almost_matrix(r, c, m):
    matrix = [["*"] * c for _ in xrange(r)]
    matrix[-1][-1] = "c"
    return matrix

def get_regular_matrix(r, c, m):
    matrix = [["."] * c for _ in xrange(r)]
    m_count = 0
    for x in xrange(r):
        if m_count == m:
            break
        for y in xrange(c):
            matrix[x][y] = "*"
            m_count += 1
            if m_count == m:
                break
        if m_count == m:
            break
    if m % c == (c - 1):
        if c == 2:
            return
        matrix[(m/c) + 1][0] = "*"
        matrix[m/c][-2] = "."
    matrix[-1][-1] = "c"
    return matrix

def get_two_rem_matrix(r, c, m):
    print "two_rem_matrix", r,c,m
    matrix = [["."] * c for _ in xrange(r)]
    to_fill = (c * (r-2))
    print "to_fill", to_fill
    m_count = 0
    for x in xrange(r):
        for y in xrange(c):
            matrix[x][y] = "*"
            m_count += 1
            if m_count == to_fill:
                break
        if m_count == to_fill:
            break
    left = m - to_fill
    y = 0
    while left != 0:
        matrix[-1][y] = "*"
        matrix[-2][y] = "*"
        left = left - 2
        y += 1
    matrix[-1][-1] = "c"
    return matrix

def get_three_rem_matrix(r, c, m):
    print "three_rem_matrix", r,c,m
    matrix = [["."] * c for _ in xrange(r)]
    to_fill = (c * (r-3))
    m_count = 0
    for x in xrange(r):
        for y in xrange(c):
            matrix[x][y] = "*"
            m_count += 1
            if m_count == to_fill:
                break
        if m_count == to_fill:
            break
    left = m - to_fill
    y = 0
    while left != 0:
        matrix[-3][y] = "*"
        left = left - 1
        if left == 0:
            break
        matrix[-2][y] = "*"
        matrix[-1][y] = "*"
        left = left - 2
        y += 1
    matrix[-1][-1] = "c"
    return matrix


# Make sure r >= c
def get_matrix(r, c, m):
    if c == 1:
        output = get_column_matrix(r, m)
        return output
    if (m == r*c -1):
        output = get_almost_matrix(r, c, m)
        return output
    if (m == (r*c - 2)) or (m == (r*c - 3)):
        return
    num_empty_lines = r - math.ceil(m / ( 1.0 * c))
    print "# empty lines", num_empty_lines,r,c,m
    if (num_empty_lines >=3):
        return get_regular_matrix(r, c, m)
    if (num_empty_lines == 2) and m % c != (c - 1):
        return get_regular_matrix(r, c, m)
    three_rem = m - ((r-3)*c)
    two_rem = m - ((r-2 )*c)
    print "three_rem, two_rem", three_rem, two_rem
    if two_rem % 2 == 0:
        return get_two_rem_matrix(r, c, m)
    if (three_rem % 3 == 0 or three_rem % 3 == 1) and ((3 * c) - three_rem) > 5:
        return get_three_rem_matrix(r, c, m)


def get_output(x, f):
    output = "Case #%s:\n" % (x,)
    r, c, m = tuple([int(x) for x in f.readline().split()])
    if r >= c:
        matrix = get_matrix(r, c, m)
    else:
        print "there", m
        matrix = get_matrix(c, r, m)
        if matrix is not None:
            matrix = zip(*matrix)
    if matrix is None:
        output += "Impossible\n"
    else:
        output += print_matrix(matrix)
    return output

def main():
    output = ""
    with open(sys.argv[1]) as f:
        t = int(f.readline())
        #print t
        for x in xrange(t):
            output += get_output(x+1, f)
    with open("output.txt", "wb") as f:
        f.write(output)

if __name__ == "__main__":
    main()