"""
Iterate through the digits looking for a dip below leading digit. At a dip,
carry from the next digit up. Proceed until complete.
"""

import sys

"""
Solve given N in str form.
"""
def solve(N):
    digits = map(int, N)
    digits.reverse()
    done = False
    while not done:
        done = True
        for i in xrange(len(digits)):
            if i == 0: continue
            if digits[i] > digits[i-1]:
                digits[i] -= 1
                digits[:i] = [9]*i
                done = False
                break
    return int("".join(map(str, reversed(digits))))

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        N = sys.stdin.readline().strip()
        print "Case #%d: %d" % (i+1, solve(N))
