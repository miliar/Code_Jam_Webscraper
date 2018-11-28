from __future__ import with_statement
import sys


# total % 3 == 0:
#   (x,x,x)
#   (x-1,x,x+1) - (*)
# total % 3 == 1:
#   (x,x,x+1)
#   (x-1,x+1,x+1) - (*)
# total % 3 == 2:
#   (x,x+1,x+1)
#   (x,x,x+2) - (*)

def solve(surprising, points, totals):
    high_scores = 0

    for total in totals:
        mod = total % 3
        x = total / 3

        if x >= points:
            high_scores += 1
        elif x + 1 >= points and mod > 0:
            high_scores += 1
        elif x + 1 >= points and mod == 0 and surprising > 0 and x > 0:
            high_scores += 1
            surprising -= 1
        elif (x + 2) >= points and mod == 2 and surprising > 0:
            high_scores += 1
            surprising -= 1

    return high_scores


with open(sys.argv[1]) as input:
    with open(sys.argv[1] + '.out', 'w') as output:
        for i in range(int(input.readline())):
            case = input.readline().strip().split()
            solution = solve(int(case[1]), int(case[2]), [int(x) for x in case[3:]])
            output.write('Case #%d: %d\n' % (i + 1, solution))