#def bool_tidy_num()
def bool_tidy_num(num):
    if num < 10:
        return True

    L = list()
    for digit in str(num):
        L.append(digit)

    for i in xrange(len(L) - 1 ):
        if L[i] > L[i + 1]:
            return False

    return True

#def solution()
def solution(t):
    n = long(t)
    i = 1
    while not bool_tidy_num(n):
        curr_digit = (n/i) % 10
        if curr_digit != 9:
            n = n - i
        else:
            i = i * 10

    return str(n)

# read case as input
t = input()

for i in xrange(1, t + 1):
    t = raw_input()
    print "Case #{}: {}".format(i, solution(t))