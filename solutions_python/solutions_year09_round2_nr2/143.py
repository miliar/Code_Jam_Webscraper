import sys

def change_replace(S):
    S = list(S)
    replacer = len(S) - 1
    replacee = -1
    for i in xrange(len(S)-1, -1, -1):
        j = i
        while j > -1:
            if S[j] < S[i]:
                break
            j -= 1
        if j == -1:
            continue
        if j > replacee:
            replacee = j
            replacer = i
    if replacee == -1:
        S.append('0')
        S.sort()
        for k in xrange(1, len(S)):
            if S[k] != '0':
                S[0], S[k] = S[k], S[0]
                break
        return S
    S[replacee], S[replacer] = S[replacer], S[replacee]
    return S[:replacee+1]+sorted(S[replacee+1:])

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for case in xrange(1, N+1):
        number = sys.stdin.readline().rstrip()
        sys.stdout.write('Case #')
        sys.stdout.write(str(case))
        sys.stdout.write(': ')
        for i in change_replace(number):
            sys.stdout.write(i)
        sys.stdout.write('\n')
