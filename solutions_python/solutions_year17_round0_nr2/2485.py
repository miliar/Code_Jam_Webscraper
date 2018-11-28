import re

def find(N):
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            return i
    return -1

def do(N):
    idx = find(N)
    if idx == -1:
        return N
    r =  '9' * (len(N)-idx-1)
    t = int(N[idx]) - 1
    r = re.sub(r'^0*', '', N[:idx] + str(t) + r)
#     print(r)
    if idx == 0 or int(N[idx-1]) <= t:
        return r
    else:
        return do(r)

T = int(input())
for i in range(1, 1+T):
    N = input()
    print('Case #%d: %s' % (i, do(N)))
