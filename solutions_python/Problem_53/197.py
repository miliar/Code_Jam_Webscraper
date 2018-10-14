def process_input(filename):
    openfile = open(filename, 'r')
    L = int(openfile.readline()[:-1])
    tests = []
    for j in range(L):
        NK = openfile.readline()
        N, K = [int(s) for s in NK.split(' ')]
        tests.append([N, K])
    openfile.close()
    return tests
             
if __name__ == '__main__':
    tests = process_input('A.in')
    X = 1
    for [N, K] in tests:
        # the state of the chain is periodic with period 2**N
        # the bulb is on at the last step before the chain 
        # reverts to its initial state
        period = 2**N
        if (K % period) == period - 1:
            state = 'ON'
        else:
            state = 'OFF'
        print 'Case #%s: %s' %(X, state)
        X += 1
