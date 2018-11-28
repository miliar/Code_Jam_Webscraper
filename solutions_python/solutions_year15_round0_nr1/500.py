#!/usr/bin/env python
import fileinput
f = fileinput.input()
T = int(f.readline())
for t in range(T):
    [S,A] = f.readline().strip().split()
    S = int(S)
    A = map(int, list(A))
    #print S, A
    stand = 0
    invite = 0
    for s in range(S+1):
        if A[s]:
            if stand < s:
                add = s - stand
                stand += add
                invite += add
            stand += A[s]
        #print s, A[s], 'stand', stand, 'invite', invite

    print 'Case #{}: {}'.format(t+1, invite)
