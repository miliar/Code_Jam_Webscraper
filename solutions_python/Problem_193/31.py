
import sys
sys.setrecursionlimit(5000)
from collections import Counter, defaultdict
from random import choice
import random

DEBUG=True

def gl():
    return sys.stdin.readline().strip()

def one_to_bin(row):
    return list(map(lambda t: t == '1', row))

def intersects(ra, rb):
    return any(a and b for (a,b) in zip(ra, rb))

def subset(ra, rb): # ra <= rb ?
    return not any(a and not b for (a,b) in zip(ra, rb))

def union(ra, rb):
    return list(a or b for (a,b) in zip(ra, rb))

def differenc(ra, rb): # ra - rb
    return list(a and not b for (a,b) in zip(ra, rb))

def factory(N, rows):
    # recursive. find minimal block, count weight, solve subproblem.

    base = 0
    while base < len(rows):
        w = rows[base]
        if not any(w):
            base += 1
        else:
            break

    if base == len(rows):
        return 0, []
        # all blank
        # return N, [(1,1)] * N

    done = False
    k = base + 1
    while k < len(rows):
        if intersects(w, rows[k]) and not subset(rows[k], w):
            w = union(w, rows[k])
            k = base + 1
            continue
        k += 1

    count = 0
    remainder = []
    for row in rows:
        if intersects(w, row):
            needed = differenc(w, row)
            dollars = len([a for a in needed if a])
            count += dollars
        else:
            new_row = [a for (j, a) in enumerate(row) if not w[j]]
            remainder += [new_row]

    # we have count, N - 
    if remainder:
        more_count, blocks = factory(len(remainder), remainder)
    else:
        more_count, blocks = 0, []

    this_block = (N - len(remainder), len([a for a in w if a]))

    return count + more_count, [this_block] + blocks

def subsets(lst):
    if not lst:
        yield []
        return
    for rst in subsets(lst[1:]):
        yield rst
        yield [lst[0]] + rst

def factory2(N, rows):
    count, blocks = factory(N, rows)
    # print 'starting count', count
    while blocks:
        squares = [(a,b) for (a,b) in blocks if a == b]
        N = N - sum(a[0] for a in squares)
        blocks = [(a,b) for (a,b) in blocks if a != b]

        if not blocks:
            break

        assert N >= 1
        # print N, blocks

        # find smallest max cover
        delta = [a - b for (a,b) in blocks]
        white = (N - sum(a[0] for a in blocks), N - sum(a[1] for a in blocks))
        white_delta = white[0] - white[1]
        
        biggest_block = (0,0)
        for k, (a, b) in enumerate(blocks):
            if max(a,b) > max(biggest_block[0], biggest_block[1]):
                biggest_block = (a,b)
                bb_index = k

        # print 'biggest', biggest_block

        other_blocks = list(blocks)
        del other_blocks[bb_index]
        smallest = N + 1
        for candidate in subsets(other_blocks):
            x = biggest_block[0] + sum(r[0] for r in candidate)
            y = biggest_block[1] + sum(r[1] for r in candidate)
            # print x, y, white_delta
            if x <= y + white[1] and y <= x + white[0] and max(x,y) < smallest:
                smallest = max(x,y)
                smallest_candidate = candidate

        # print smallest, smallest_candidate
        more_ones = smallest * smallest - sum(x * y for (x,y) in smallest_candidate) - biggest_block[0] * biggest_block[1]
        # print 'more', more_ones
        count += more_ones

        N -= smallest
        for block in smallest_candidate + [biggest_block]:
            t = blocks.index(block)
            del blocks[t]

    return count + N

def main():
    T = int(gl())
    for k in range(T):
        N = int(gl())
        matrix = []
        for _ in range(N):
            matrix += [one_to_bin(gl())]
        # print matrix
        solution = factory2(N, matrix)
        print 'Case #' + str(k+1) + ': ' + str(solution)

if __name__ == '__main__':
    main()

