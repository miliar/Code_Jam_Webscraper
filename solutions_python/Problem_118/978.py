import sys
import pprint
import math

def is_palindrome(val):
    fail = False
    for j in range(len(val)):
        if val[j] != val[len(val) - j - 1]:
            fail = True
            break
    return fail == False

def main():
    t = int(sys.stdin.readline())
    for k in range(t):
        line = sys.stdin.readline().split()
        a = int(line[0])
        b = int(line[1])
        ans = 0
        for i in range(a, b + 1):
            s = int(math.sqrt(i))
            if s * s != i:
                continue
            if is_palindrome(str(s)) == False:
                continue
            s = str(i)
            if is_palindrome(s) == False:
                continue
            ans += 1
        print 'Case #{}: {}'.format(k + 1, ans)

main()