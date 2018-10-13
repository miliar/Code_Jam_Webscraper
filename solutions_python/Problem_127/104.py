import sys

sys.stdin = open('B-small-attempt0.in', 'r')
sys.stdout = open('op.txt', 'w')


def solve(tc):

    [x, y] = raw_input().split(' ')
    [x, y] = [int(x), int(y)]

    ans = ''

    if x > 0:
        for i in range(x):
            ans = ans + 'WE'
    else:
        for i in range(-x):
            ans = ans + 'EW'

    if y > 0:
        for j in range(y):
            ans = ans + 'SN'
    else:
        for j in range(-y):
            ans = ans + 'NS'


    print 'Case #' + str(tc) + ': ' + ans


def main():
    t = int(raw_input())
    for tc in range(1, t+1):
        solve(tc)

main()
