T = int(raw_input())

for x in xrange(1, T+1):
    N = int(raw_input())
    N = list(str(N))
    l = len(N)
    i = l - 2
    while i >= 0:
        if N[i] > N[i+1]:
            N[i] = str(int(N[i]) - 1)
            j = i + 1
            while j < l and N[j] != '9':
                N[j] = '9'
                j += 1
        i -= 1
    print "Case #{}: {}".format(x, int(''.join(N)))