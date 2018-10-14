#Fair and Square
import sys
import pdb

def is_palindrome(x):
    x = str(x)
    n = len(x)
    for i in xrange(n / 2):
        if x[i] != x[n - i - 1]:
            return False
    return True

def make_palindrome1(x):
    x = list(str(x))
    y = x[:]
    y.reverse()
    x += y[1:]
    return int("".join(x))

def make_palindrome2(x):
    x = list(str(x))
    y = x[:]
    y.reverse()
    x += y
    return int("".join(x))

def get_fair1(n):
    fair = []
    for x in xrange(n):
        y = make_palindrome1(x) ** 2
        if is_palindrome(y):
            fair.append(y)
    return fair

def get_fair2(n):
    fair = []
    for x in xrange(n):
        y = make_palindrome2(x) ** 2
        if is_palindrome(y):
            fair.append(y)
    return fair

def find(x, arr):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) / 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')

    fair = get_fair1(10000) + get_fair2(1000)
    fair.sort()
    T = int(infile.readline().strip())
    for num in xrange(1, T+1):
        A, B = map(int, infile.readline().strip().split())
        begin = find(A, fair)
        end = find(B, fair)
        if end < len(fair) and fair[end] == B:
            end += 1
        print >> outfile, 'Case #%d: %d' % (num, end - begin)

    infile.close()
    outfile.close()

