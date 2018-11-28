#! /usr/local/bin/python

def solve(stack, k):
    bstack = [e == '+' for e in stack]
    flips = 0
    for i in xrange(len(stack)-k+1):
        if not bstack[i]:
            flips += 1
            for j in xrange(i,i+k):
                bstack[j] = not bstack[j]

    if all(bstack):
        return flips
    else:
        return 'IMPOSSIBLE'


n = int(raw_input())

cases = []
for i in range(n):
    cases.append(raw_input().strip())

output = []
for i, case in enumerate(cases):
    stack, k = case.split()
    output.append('Case #{}: {}'.format(i+1, solve(stack, int(k))))

print '\n'.join(output)
