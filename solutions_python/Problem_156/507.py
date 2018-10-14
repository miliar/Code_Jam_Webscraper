from math import ceil
import sys
sys.setrecursionlimit(10000)

def read_list_of(numtype):
    return map(numtype, raw_input().split())

def solve(l):
    l.sort(reverse=True)
    memo = {}
    return solve_sorted(l, memo)

def solve_sorted(l, memo):
    if tuple(l) in memo:
        return memo[tuple(l)]


    if l[0] == 1:
        return 1

    old_l0 = l[0]
    solutions = []

    for i in xrange(1, old_l0/2 + 1):
        new_l = l[:]
        new_l[0] -= i
        new_l.append(i)
        new_l.sort(reverse=True)

        solutions.append(new_l)

    solutions_cost = [solve_sorted(s, memo) for s in solutions]


    if len(solutions_cost) == 0:
        result = l[0]
    else:
        result = min(1+min(solutions_cost), l[0])

    memo[tuple(l)] = result
    return result
#
# print solve([9]) == 5
# print solve([9, 9]) == 7
# print solve([9, 9, 9]) == 8
# print solve([9, 9, 9, 9]) == 9
# print solve([9, 9, 9, 9, 9]) == 9
# print solve([9, 1, 2, 1, 1]) == 5
#
# print solve([3]) == 3
# print solve([1,2,1,2]) == 2
# print solve([4]) == 3
#
# print solve([1,2,4]) == 3

def main():
    for case_number in xrange(int(raw_input())):
        num_diners = raw_input()
        l = read_list_of(int)

        result = solve(l)

        print 'Case #%d: %s' % (case_number+1, result)

main()