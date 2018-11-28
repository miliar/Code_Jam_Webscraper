import sys

sys.stdin = open('C-small-attempt0.in', 'r')
sys.stdout = open('op.out', 'w')

'''
def isPalin(s):
    if s == '':
        return True
    return s[0] == s[len(s)-1] and isPalin(s[1:len(s)-1])

psquares = []
for i in range(10000001):
    if isPalin(str(i)) and isPalin(str(i*i)):
        psquares.append(i*i)
'''

psquares = [0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004,
            100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404,
            10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L,
            1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L,
            1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L,
            4000008000004L, 4004009004004L]

def solve(tc):
    global psquares

    [a, b] = raw_input().split(' ')
    [a, b] = [int(a), int(b)]

    ai = bi = 0

    for i in range(len(psquares)):
        if psquares[i] >= a:
            ai = i
            break

    for i in range(len(psquares)):
        if psquares[i] > b:
            bi = i
            break

    print 'Case #' + str(tc) + ': ' + str(bi - ai)


def main():
    t = int(raw_input())
    for tc in range(1, t+1):
        solve(tc)

main()
