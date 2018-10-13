#!/usr/bin/python2.5
# Solution to Google Code Jam 08 Round 1B Problem A
# Matt Giuca

# Usage: ./probA.py < inputfile > outputfile

import sys
import copy

DEBUG = False

def parse(file=sys.stdin):
    """
    (Generator) Read input file from filename or file or stdin,
    return a structure.
    Yields tuple of n, A, B, C, D, x0, y0, M.
    """
    if isinstance(file, basestring):
        file = open(file)
        toclose = True
    else:
        toclose = False
    n = int(file.readline().strip())
    for i in range(n):
        yield map(int, file.readline().strip().split())
    if toclose:
        file.close()

def solve_case(n, A, B, C, D, x0, y0, M):
    basketdict = {}
    total = 0
    for b in baskets():
        basketdict[b] = 0
    for x,y in gen_trees(n, A, B, C, D, x0, y0, M):
        put_tree_in_basket(basketdict, (x,y))
    for a,b,c in basket_selection():
        # Backup dict
        tempdict = copy.copy(basketdict)
        num = 1
        # Choose one from each basket A, B, C (which could be the same basket)
        # without replacement.
        num *= tempdict[a]
        if tempdict[a] > 0: tempdict[a] -= 1
        num *= tempdict[b]
        if tempdict[b] > 0: tempdict[b] -= 1
        num *= tempdict[c]
        total += num

    return total // 6

def gen_trees(n, A, B, C, D, x0, y0, M):
    """
    Generates the position of each tree.
    """
    X = x0; Y = y0
    yield X, Y
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        yield X, Y

def put_tree_in_basket(basketdict, coord):
    """
    A basketdict maps basket names (2-tuples of ints range(0,3)) to counts -
    number of trees in that basket.
    """
    x,y = coord
    basket = x%3,y%3
    if basket in basketdict:
        basketdict[basket] += 1
    else:
        basketdict[basket] = 1

def baskets():
    """
    Generator. Yields all baskets.
    """
    for i in range(0,3):
        for j in range(0,3):
            yield i,j

def basket_selection():
    """
    Generator. Yields 3-tuples of baskets (2-tuples) which are valid
    combinations.
    """
    for x1,y1 in baskets():
        for x2,y2 in baskets():
            for x3,y3 in baskets():
                # Pick only the ones where the sums of xs and sums of ys both
                # add to a multiple of 3.
                if (x1+x2+x3) % 3 == 0 and (y1+y2+y3) % 3 == 0:
                    yield ((x1,y1), (x2,y2), (x3,y3))

def main(file=sys.stdin):
    """
    Processes input, prints output to stdout.
    """
    i = 0
    for info in parse(file):
        i += 1
        answer = solve_case(*info)
        print("Case #%d: %d" % (i, answer))

if __name__ == "__main__":
    main()
