numCases = int(raw_input())
pos1 = 0
pos2 = 0
S = ""
K = 0
last = 1


for case in range(numCases):
    done = 0
    impossible = 0
    count = 0
    S = raw_input()
    a = S.split()
    S = a[0]
    K = int(a[1])
    for i in range(0, len(S)):
        pos1 = i
        if (S[i]=='-'):
            break
    for i in range(len(S)-1, -1, -1):
        pos2 = i
        if (S[i]=='-'):
            break
    while 1:
        if (pos1==pos2):
            if (K>1):
                impossible = 1
                break;
            if (K==1):
                break
        if (pos2 > pos1):
            overlap = 0
            diff = pos2-pos1+1
            if (diff < (2*K) and diff >= K):
                overlap = 2*K-diff
                if (overlap == K):
                    same = 1
                    for i in range(pos1, pos1+K):
                        if (S[i]=='+'):
                            same = 0
                            break
                    if same:
                        count = count+1
                        break
                    else:
                        impossible = 1
                        break
                else:
                    start = pos2-K+1
                    ch = S[start]
                    same = 1
                    for i in range(start, start+overlap):
                        if not(S[i]==ch):
                            same = 0
                            break
                    if not same:
                        impossible = 1
                        break
            if (diff < (2*K) and diff < K):
                impossible = 1
                break
            new = ""
            for i in range(pos1, pos1+K):
                if S[i]=='-':
                    new = new + '+'
                else:
                    new = new + '-'
            S = S[:pos1] + new + S[pos1+K:]
            count = count+1
            new = ""
            for i in range(pos2, pos2-K, -1):
                if S[i]=='-':
                    new = '+' + new
                else:
                    new = '-' + new
            S = S[:pos2-K+1] + new + S[pos2+1:]
            count = count+1
            for i in range (pos1, len(S)):
                pos1 = i
                if (S[i]=='-'):
                    break;
            for i in range (pos2, -1, -1):
                pos2 = i
                if (S[i]=='-'):
                    break;
        else:
            break
    print "case #"+str(case+1)+':',
    if (impossible):
        print "IMPOSSIBLE"
    else:
        print count
