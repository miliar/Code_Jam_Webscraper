import pp
import sys

def calc_time(C, F, X):
    K = 2.0
    result = X / K
    total = 0
    for i in xrange(int(X / C)):
        total += C / K
        time = total + X / (K + F)
        result = min(result, time)
        K += F

    return result

job_server = pp.Server()

f = open('B-large.in', 'r')
T = int(f.readline()) + 1

jobs = []
for test in xrange(1, T):
    C, F, X = map(float, f.readline().strip().split())

    jobs.append(job_server.submit(calc_time, (C, F, X)))

f.close()

open('output.txt', 'w').write('\n'.join(['Case #%d: %s' % (i + 1, str(job())) for i, job in enumerate(jobs)]))
