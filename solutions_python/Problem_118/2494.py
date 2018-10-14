import math

def palindrome(a):
    a = str(a)
    return a == a[::-1]

def solve_test(A, B):
    n = 0
    for i in xrange(A, B+1):
        if palindrome(i):
            si = math.sqrt(i)
            if si == int(si) and palindrome(int(si)):
                n += 1
    return n

def solve():
    T = input()

    for test in range(T):
        l = raw_input()
        A, B = map(int, l.split())

        sol = solve_test(A, B)

        print "Case #%d: %d" % (test + 1, sol)

solve()

