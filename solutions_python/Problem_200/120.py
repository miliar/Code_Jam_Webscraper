def f(S):
    S = list(S)
    x = int(S[-1])
    for i in range(len(S)-2, -1, -1):
        ii = int(S[i])
        if ii > x:
            newS = S[:i] + [str(ii-1)] + ['9'] * (len(S)-i-1)
            return f(newS)
        elif ii < x:
            x = ii
    if S[0] == '0':
        return '9' * (len(S)-1)
    else:
        return ''.join(S)

fin = open('b2.in')
fout = open('b2.out','w')

T = int(fin.readline())

for t in range(T):
    fout.write('Case #%s: %s\n' % (t+1, f(fin.readline()[:-1])))