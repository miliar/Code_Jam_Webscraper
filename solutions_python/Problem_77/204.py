import sys
import math

invfact = [1., 1.]
while len(invfact)<2000:
    invfact.append(invfact[-1] / len(invfact))

invfactpm = [1., -1.]
while len(invfactpm)<2000:
    invfactpm.append(-invfactpm[-1] / len(invfactpm))

fn = [1., 0.]
while len(fn)<2000:
    fn.append(fn[-1] + invfactpm[len(fn)])
    
an = [0.]
while len(an)<2000:
    an.append((1+sum(an[k]*fn[k]*invfact[len(an)-k] for k in range(len(an)))) / (1-fn[len(an)]))

def solve(array):
    misplaced = len([i for i in range(len(array)) if array[i] != i+1])
    return an[misplaced]

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    M = int(line[0])
    line = input.readline().strip(' \r\n\t').split()
    assert len(line)==M
    vals = [int(s) for s in line]
    res = solve(vals)
    return str(res)

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
