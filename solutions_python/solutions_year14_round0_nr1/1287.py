import sys
readline = sys.stdin.readline
def solve_case(n):
    row1 = int(readline())
    m1 = [map(int, readline().split()) for _ in range(4)]
    row2 = int(readline())
    m2 = [map(int, readline().split()) for _ in range(4)]

    guess = set(m1[row1-1]) & set(m2[row2-1])
    i = len(guess)
    if i == 1:
        print "Case #%d: %d" % (n, guess.pop())
    elif i > 1:
        print "Case #%d: Bad magician!" % n
    else:
        print "Case #%d: Volunteer cheated!" % n

if __name__ == '__main__':
    c = int(readline())
    for n in range(c):
        solve_case(n+1)
