import sys

#sys.stdin = open('C-large-1.in', 'r')
sys.stdin = open('A-small-attempt0.in', 'r')
sys.stdout = open('op.out', 'w')



def solve(tc):
    [r, t] = raw_input().split(' ')
    [r, t] = [int(r), int(t)]

    i = 0
    cnt = 0
    ans = 0.0
    PI = 3.14159265359

    while (ans <= t):
        ans = ans + (2*r) + i + (i+1)
        i = i + 2
        cnt = cnt + 1

    print 'Case #' + str(tc) + ': ' + str(cnt-1)



def main():
    T = int(raw_input())
    for tc in range(1, T+1):
        solve(tc)

main()
