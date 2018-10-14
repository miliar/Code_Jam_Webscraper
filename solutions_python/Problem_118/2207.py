from math import sqrt

def is_fair_and_square(num):
    def is_palindrome(n):
        def is_int(k):
            if k - int(k) == 0:
                return True
            return False
        if not is_int(n):
            return False
        st = str(int(n))
        rev = ""
        for ch in reversed(st):
            rev += ch
        if rev != st:
            return False
        else:
            return True
    if is_palindrome(num) and is_palindrome(sqrt(num)):
        return True
    else:
        return False

def fas_in_range(A, B):
    fas = 0
    for i in range(A, B+1):
        if is_fair_and_square(i):
            fas += 1
    return fas

lines = list(open("input.dat"))
lines = map(lambda x: x.rstrip(), lines)
N = int(lines[0])
for i in range(1, N+1):
    [A, B] = map(int, lines[i].split(" "))
    print "Case #" + str(i) + ": " + str(fas_in_range(A, B))
