import sys
import math

precomputed = []

def square(num):
    if num == 1:
        return 1
    x = num // 2
    seen = set([x])
    while x * x != num:
        x = (x + (num // x)) // 2
        if x in seen:
            return x
        seen.add(x)
    return x

def is_square_of_a_palindrome(num):
    sqr = square(num)
    if sqr and is_a_palindrome(long(sqr)):
            return True
    return False

def is_a_palindrome(inum):
    num = str(inum)
    return num == num[::-1]

def precompute(A, B):
    squares = (n**2 for n in xrange(square(A), square(B) + 1))
    for val in squares:
        if is_a_palindrome(val) and is_square_of_a_palindrome(val):
            #print val
            precomputed.append(val)

def solve(A, B):
    count = 0
    for i in precomputed:
        if i >= A and i <= B:
            count += 1
    return count

def main(filename):
    with open(filename, "r") as f:
        T = int(f.readline().strip())
        for t in xrange(T):
            vals = f.readline().strip().split(" ")
            sol = solve(long(vals[0]), long(vals[1]))
            print "Case #%d: %s" % (t+1, sol)


if __name__ == "__main__":
    precompute(1, 1000000000000000)
    #print precomputed
    main(sys.argv[1])
