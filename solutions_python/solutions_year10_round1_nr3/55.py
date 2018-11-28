def process_input(filename):
    openfile = open(filename, 'r')
    T = int(openfile.readline()[:-1])
    tests = []
    for j in range(T):
        line = openfile.readline()
        A1, A2, B1, B2 = [long(s) for s in line.split(' ')]
        tests.append([A1, A2, B1, B2])
    openfile.close()
    return tests
             
def wins(A, B):
    if A == B:
        return False
    if A < B:
        temp = A
        A = B
        B = temp
    q = A // B
    if q > 1:
        return True
    return not wins(B, A-B)


if __name__ == '__main__':
    tests = process_input('C.in')
    T = 1
    for [A1, A2, B1, B2] in tests:
        winning = 0
        for A in xrange(A1, A2+1):
            for B in xrange(B1, B2+1):
                if wins(A, B):
                    winning += 1
        print 'Case #%s: %s' %(T, winning)
        T += 1
