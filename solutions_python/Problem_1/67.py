import sys

def do_test(input, test):
    S = int(input.readline())
    engines = []
    for i in range(S):
        engines.append(input.readline()[:-1])
    Q = int(input.readline())

    index = {}
    for x in range(S):
        index[engines[x]] = x

    answer = 0
    state = [0]*S
    state0 = S

    for i in range(Q):
        query = input.readline()[:-1]
        if query in index:
            ind = index[query]
            if state[ind]==0:
                if state0>1:
                    state[ind] = 1
                    state0 -= 1
                else:
                    answer += 1
                    for x in range(S):
                        state[x] = 0
                    state[ind] = 1
                    state0 = S-1
    print 'Case #%(case)d: %(answer)d' % {'case': test+1, 'answer': answer}
                        


input = sys.stdin

N = int(input.readline())

for test in range(N):
    do_test(input, test)

