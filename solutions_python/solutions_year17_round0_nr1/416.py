def flips(s):
    K = int(s[1])
    S = list(s[0])
    n=0 # number of flips
    # loop over all pancakes:
    for i in range(0,len(S)-K+1):
        # S[i:i+K] - the piece which we modify
        # loop over K pancakes:
        if S[i]=='-':
            for j in range(i, i+K):
                S[j]=flip(S[j])
            n+=1
            #print S
    # verify if everything is good:
    if S.count('-')>0:
        return 'IMPOSSIBLE'
    return `n`

def flip(sign):
    if sign=='-':
        return '+'
    return '-'

f = open('input.in', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    tcs.append(f.readline().split(' '))

f.close()
f = open('output.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s\n" % (i+1, flips(tcs[i])))
f.close()

