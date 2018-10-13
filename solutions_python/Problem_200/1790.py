def sol(N):
    j = len(N) - 1
    for i in xrange(0, len(N) - 1):
        if N[i] > N[i + 1]:
            j = i
            break
    if j == len(N) - 1:
        return int("".join(N))
    else:
        temp = int("".join(N[:j+1]) + '0'*(len(N)-j-1))
        return sol(map(lambda x: x, str(temp-1)))


t = long(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N = raw_input()
    N = map(lambda x: x, N) 
    print "Case #{}: {}".format(i, sol(N))
