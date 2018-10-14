import sys

num_cases = int(sys.stdin.readline())

def is_palindrome(num):
    num_str = str(num)
    for i in range(len(num_str) / 2):
        if num_str[i] != num_str[-(i+1)]:
            return False
    return True

def find_fair_n_squares(A, B):
    A_sqr = int(A ** 0.5)
    while (A_sqr ** 2) < A:
        A_sqr += 1
    B_sqr = int(B ** 0.5)

    count = 0
    for n in xrange(A_sqr, B_sqr + 1):
        n_sq = n ** 2
        if not (is_palindrome(n) and is_palindrome(n_sq)):
            continue
        if n_sq > B:
            break
        count += 1
    return count

for n in xrange(num_cases):
    A, B = [int(e) for e in sys.stdin.readline().strip().split()]

    print "Case #%s: %s" % (n+1, find_fair_n_squares(A, B))
    n += 1
