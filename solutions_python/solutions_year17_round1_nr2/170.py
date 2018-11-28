from itertools import permutations
import math

def legal(r1, r2, q1, q2):
    for x in xrange(int(math.ceil(q1/1.1 / r1)), int(math.floor(q1/0.9 / r1))+1):
        if 0.9 * x * r2 <= q2 <= 1.1 * x * r2:
            return True
    return False

IN = open('input.txt', 'r')
OUT = open('output.txt', 'w')

NUM_TESTS = int(IN.readline())

for test in xrange(NUM_TESTS):
    N, P = map(int,IN.readline().split())
    R = map(int,IN.readline().split())
    Q = []
    for _ in xrange(N):
        Q.append(map(int,IN.readline().split()))
        
    if N == 1:
        answer = 0
        for q in Q[0]:
            x = int(q/0.9 / R[0])
            if 0.9 * x * R[0] <= q <= 1.1 * x * R[0]:
                answer += 1
    if N == 2:
        answer = 0
        for perm in permutations(range(P)):
            count = 0
            for i, j in enumerate(perm):
                if legal(R[0], R[1], Q[0][i], Q[1][j]):
                    count += 1
            if count > answer:
                answer = count
    
    OUT.write('Case #{}: {}\n'.format(test+1, answer))
    print test+1, answer

IN.close()
OUT.close()
