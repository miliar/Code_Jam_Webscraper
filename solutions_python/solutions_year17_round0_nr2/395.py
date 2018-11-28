def printN(N):
    if N[0] == 0:
        print ''.join(map(str, N[1:]))
    else:
        print ''.join(map(str, N))


def main(index):
    print 'Case #%d:' % index,
    N = raw_input()
    if len(N) == 1:
        print N
        return
    N = map(int, list(N))
    for index, (x, y) in enumerate(zip(N[:-1], N[1:])):
        if x > y:
            for j in xrange(index+1, len(N)):
                N[j] = 9
            break
    else:
        printN(N)
        return
    N[index] -= 1
    while index !=0 and N[index-1] > N[index]:
        N[index] = 9
        N[index-1] -= 1
        index -= 1
    printN(N)



T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
