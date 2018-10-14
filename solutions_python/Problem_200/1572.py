import sys
sys.setrecursionlimit(1000000)

def function(n):
    if n < 10:
        return n
    string = str(n)
    is_tidy = True
    for i in xrange(len(string)-1, 0, -1):
        if string[i-1] > string[i]:
            n = string[:i-1] + str(int(string[i-1]) - 1) + '9' * (len(string[i+1:]) + 1)
            is_tidy = False
            break
    if is_tidy:
        return n
    else:
        return function(int(n))

T = int(raw_input().strip())  # read a line with a single integer

for i in xrange(1, T + 1):
    n = int(raw_input().strip())  # read input
    print "Case #{}: {}".format(i, function(n))
