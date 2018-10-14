import numpy as np


def flip(s):
    sout = ['+' if x == '-' else '-' for x in s]
    return np.array(sout)


if __name__ == '__main__':
    t = int(raw_input())
    for i in np.arange(t):
        s, K = raw_input().split(" ")
        s = np.array([x for x in s])
        K = int(K)

        cnt = 0
        for j in np.arange(len(s)-K+1):
            if s[j] == '-':
                cnt += 1
                s[j:j+K] = flip(s[j:j+K])
        if np.any(s[-K:] != np.array(['+' for x in np.arange(K)])):
            output = 'IMPOSSIBLE'
        else:
            output = str(cnt)
        print 'Case #%d: '%(i+1)+output
