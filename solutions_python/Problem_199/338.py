def flop_str(S, K):
    target = S[:K]
    flopPart = ''
    for c in target:
        flopPart += flip(c)
    return flopPart + S[K:]

def flip_times(S, K):
    flipCount = 0
    while len(S) >= K:
        if S[0] == '+':
            S = S[1:]
        else:
            S = flop_str(S, K)
            flipCount += 1
            S = S[1:]
    if '-' in S:
        return 'IMPOSSIBLE'
    else:
        return str(flipCount)

#main

#input
import os
os.chdir(r'C:\codejam\a')
FILENAME = r'A-large.in'
f = open(FILENAME)
lines = f.readlines()
f.close()

#calc
T = int(lines.pop(0)[:-1])
ans = ''
flip = lambda c: ('+','-')[c == '+']
for i in range(T):
    S, K = lines.pop(0)[:-1].split()
    K = int(K)
    ansline = 'Case #' + str(i+1) + ': ' + flip_times(S, K)
    ans += ansline + '\n'

#output
fout = open('A-large.out', 'wt')
print(ans, file = fout)
fout.close()
