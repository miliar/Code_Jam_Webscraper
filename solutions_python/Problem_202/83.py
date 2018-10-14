import logging
import Queue as Q
import math
import pprint

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def check_and_remove(grid, r, c, s):
    if r >=0 and r < len(grid) and c >=0 and c < len(grid):
        if s in grid[r][c]:
            grid[r][c].remove(s)
        if 'o' in grid[r][c]:
            grid[r][c].remove('o')

def remove_x(grid, r, c):
    for i in xrange(1, len(grid)):
        check_and_remove(grid, r+i, c+i, '+')
        check_and_remove(grid, r-i, c-i, '+')
        check_and_remove(grid, r+i, c-i, '+')
        check_and_remove(grid, r-i, c+i, '+')

def remove_plus(grid, r, c):
    for i in xrange(1, len(grid)):
        check_and_remove(grid, r, c+i, 'x')
        check_and_remove(grid, r, c-i, 'x')
        check_and_remove(grid, r+i, c, 'x')
        check_and_remove(grid, r-i, c, 'x')

def remove_symbol(grid, r, c, s):
    if s == '+':
        grid[r][c].remove('+')
        remove_x(grid, r, c)
    elif s == 'x':
        grid[r][c].remove('x')
        remove_plus(grid, r, c)
    elif s == 'o':
        grid[r][c].remove('o')
        if 'x' in grid[r][c]:
            grid[r][c].remove('x')
        if '+' in grid[r][c]:
            grid[r][c].remove('+')
        remove_x(grid, r, c)
        remove_plus(grid, r, c)
    else:
        assert(False)

def compute(n, constriants):
    result = dict()
    score = 0

    grid = [[set() for _ in xrange(n)] for _ in xrange(n)]
    result_grid = [['.' for _ in xrange(n)] for _ in xrange(n)]
    for r in grid:
        for c in r:
            c.add('+')
            c.add('x')
            c.add('o')

    for key in constriants:
        r, c = key
        result_grid[r][c] = constriants[key]
        remove_symbol(grid, r, c, constriants[key])
        if constriants[key] == '+' or constriants[key] == 'x':
            score += 1
        elif constriants[key] == 'o':
            score += 2
        else:
            assert(False)

    # for r in grid:
    #     print r

    for r in xrange(len(grid)):
        for c in xrange(len(grid)):
            # Cannot put model here
            if len(grid[r][c]) == 0:
                continue
            greedy_choice = grid[r][c].pop()
            grid[r][c].add(greedy_choice)
            if 'o' in grid[r][c]:
                greedy_choice = 'o'
            if (r,c) not in constriants:
                result_grid[r][c] = greedy_choice
                result[(r,c)] = greedy_choice
                remove_symbol(grid, r, c, greedy_choice)
                if greedy_choice == '+' or greedy_choice == 'x':
                    score += 1
                elif greedy_choice == 'o':
                    score += 2
                else:
                    assert(False)
            elif constriants[(r, c)] != greedy_choice:
                result_grid[r][c] = greedy_choice
                result[(r,c)] = greedy_choice
                remove_symbol(grid, r, c, greedy_choice)
                score += 1

    # for r in grid:
    #     print r
    #
    # for r in result_grid:
    #     print r

    return score, len(result), result

def compute_2(n, constriants):
    result_grid = [['.' for _ in xrange(n)] for _ in xrange(n)]
    col_set = set()
    row_set = set()
    sum_set = set()
    diff_set = set()
    for i in xrange(n):
        col_set.add(i)
        row_set.add(i)
    for i in xrange(2*n-1):
        sum_set.add(i)
    for i in xrange(-n+1, n):
        diff_set.add(i)

    cur_score = 0
    for key in constriants:
        r, c = key
        s = constriants[key]
        if s == 'x' or s == 'o':
            row_set.remove(r)
            col_set.remove(c)
        if s == '+' or s =='o':
            sum_set.remove(r+c)
            diff_set.remove(r-c)
        result_grid[r][c] = s
        cur_score += 2 if s == 'o' else 1

    result = dict()

    assert(len(row_set) == len(col_set))
    extra_cross = min(len(row_set), len(col_set))
    row_list, col_list = list(row_set), list(col_set)
    for i in xrange(extra_cross):
        r, c = row_list[i], col_list[i]
        if result_grid[r][c] == '.':
            result[(r, c)] = 'x'
            result_grid[r][c] = 'x'
        elif result_grid[r][c] == '+':
            result[(r, c)] = 'o'
            result_grid[r][c] = 'o'
        else:
            print result[(r,c)]
            assert(False)
        cur_score += 1

    for i in xrange(n-1, -1, -1):
        diff = i
        if diff in diff_set:
            sum_to_be_deleted = None
            for su in sum_set:
                if (su+diff)%2!=0:  # Not valid combination
                    continue
                r = (su+diff)/2
                c = (su-diff)/2
                if r >= 0 and r < n and c >=0 and c < n:
                    cur_score += 1
                    if result_grid[r][c] == '.':
                        result[(r,c)] = '+'
                        result_grid[r][c] = '+'
                    elif result_grid[r][c] == 'x':
                        result[(r,c)] = 'o'
                        result_grid[r][c] = 'o'
                    else:
                        print result[(r,c)]
                        assert(False)
                    diff_set.remove(diff)
                    sum_to_be_deleted = su
                    break
            if sum_to_be_deleted:
                sum_set.remove(sum_to_be_deleted)
        diff = -i
        if diff in diff_set:
            sum_to_be_deleted = None
            for su in sum_set:
                if (su+diff)%2!=0:  # Not valid combination
                    continue
                r = (su+diff)/2
                c = (su-diff)/2
                if r >= 0 and r < n and c >=0 and c < n:
                    cur_score += 1
                    if result_grid[r][c] == '.':
                        result[(r,c)] = '+'
                        result_grid[r][c] = '+'
                    elif result_grid[r][c] == 'x':
                        result[(r,c)] = 'o'
                        result_grid[r][c] = 'o'
                    else:
                        print result[(r,c)]
                        assert(False)
                    diff_set.remove(diff)
                    sum_to_be_deleted = su
                    break
            if sum_to_be_deleted:
                sum_set.remove(sum_to_be_deleted)

    # print "col_set: ",col_set
    # print "row_set: ",row_set
    # print "sum_set: ",sum_set
    # print "diff_set: ",diff_set

    # for r in result_grid:
    #     print r

    return cur_score, len(result), result

t = int(raw_input())
for i in xrange(1, t + 1):
    logging.info("Solving case: {}".format(i))

    n,m = [int(s) for s in raw_input().split(" ")]
    # print "Case #{}: {} {}".format(i, n + m, n * m)
    constriants = {}
    for j in xrange(m):
        s,r,l = [x for x in raw_input().split(" ")]
        constriants[(int(r)-1, int(l)-1)] = s
    pts, num_changes, changes = compute_2(n, constriants)
    print "Case #{}: {} {}".format(i, pts, num_changes)
    for c in changes:
        print changes[c], c[0]+1, c[1]+1
