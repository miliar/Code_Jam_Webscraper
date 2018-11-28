# Julie
# 30.04.2017
# Round 1C
# "Core Training"

from time import time

def Probability_K_of_N(probabilities, K, current):
    if K == 0:
        return reduce(lambda x, y: x*y, list(1 - p for p in probabilities[current:]))
    if K == len(probabilities) - current:
        return reduce(lambda x, y: x*y, list(p for p in probabilities[current:]))
    assert K < len(probabilities) - current and current < len(probabilities) - 1
    return (Probability_K_of_N(probabilities, K - 1, current + 1) * probabilities[current] + 
            Probability_K_of_N(probabilities, K, current + 1) * (1 - probabilities[current]))

def C_n_k(N, K):
    numenator = 1
    denominator = 1
    m = min(K, N - K)
    for i in range(m):
        numenator *= (N - i)
        denominator *= (i + 1)
    return numenator / denominator

def CoreTraining(K, U, probabilities):
    probabilities.sort()
    i = len(probabilities) - K
    while i < len(probabilities) - 1 and U > 0:
        diff = probabilities[i + 1] - probabilities[i]
        units_spent = min(diff * (i + 1), U) / (i + 1)
        for j in range(i + 1):
            probabilities[j] += units_spent
            assert probabilities[j] <= 1
        U -= units_spent * (i + 1)
        i += 1
    if U > 0:
        for j in range(len(probabilities) - K, len(probabilities)):
            probabilities[j] = min(probabilities[j] + U / K, 1)
    #print probabilities
    return sum(Probability_K_of_N(probabilities, P, 0) for P in range(K, len(probabilities) + 1))

#inpath = "C-sample.in"
#inpath = "C-large.in"
#inpath = "simulated.in"
inpath = "C-small-1-attempt0.in"
outpath = "C.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()

T = int(fin.readline())
for case in range(1, T+1):
    N, K = map(int, fin.readline().split())
    U = float(fin.readline())
    probabilities = (map(float, fin.readline().split()))
    assert len(probabilities) == N

    result = CoreTraining(K, U, probabilities)
    #print result
    fout.write("Case #%d: %.6f\n" % (case, result))

fin.close()
fout.close()
print "time elapsed: %.4f" % (time() - timestart)
