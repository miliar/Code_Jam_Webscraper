def solve(AC, AJ, C, D, J, K):
    print AC, AJ, C, D, J, K
    S = ['.']*1440
    for i in range(AC):
        for j in range(C[i], D[i]):
            S[j] = 'C'
    for i in range(AJ):
        for j in range(J[i], K[i]):
            S[j] = 'J'
    for i in range(24):
        print ''.join(S[i*60:(i+1)*60])
    d = []
    c = 1
    for i in range(1440):
        if S[i] != S[(i+1) % 1440]:
            d.append([S[i], c])
            c = 1
        else:
            c += 1
    if S[0] == S[-1]:
        d[0][1] += c-1
    print d
    # how many mins used:
    minC = 0
    minJ = 0
    for i in d:
        if i[0] == 'C':
            minC += i[1]
        if i[0] == 'J':
            minJ += i[1]
    print minC, minJ
    # find smallest gaps:
    while minC <= 720 and minJ <= 720:
        chg = 0
        mini = -1
        mind = 9999
        # Cs:
        for i in range(len(d)):
            if d[i][0] == '.' and d[i-1][0] == 'C' and d[(i+1)%len(d)][0] == 'C':
                if d[i][1] < mind:
                    mind = d[i][1]
                    mini = i
        if mind <= 720-minC:
            d[mini][0] = 'C'
            minC += mind
            chg = 1
        # Js:
        mini = -1
        mind = 9999
        # Cs:
        for i in range(len(d)):
            if d[i][0] == '.' and d[i - 1][0] == 'J' and d[(i + 1) % len(d)][0] == 'J':
                if d[i][1] < mind:
                    mind = d[i][1]
                    mini = i
        if mind <= 720 - minJ:
            d[mini][0] = 'J'
            minJ += mind
            chg = 1
        # print d, mini, chg
        if chg == 0:
            break
    print d
    ans = 0
    for i in range(len(d)):
        if d[i][0] != d[i-1][0]:
            ans += 1
    for i in range(len(d)):
        if d[i][0] == '.' and d[i - 1][0] == 'C' and d[(i + 1) % len(d)][0] == 'J':
            ans -= 1
        if d[i][0] == '.' and d[i - 1][0] == 'J' and d[(i + 1) % len(d)][0] == 'C':
            ans -= 1
    return ans


def main():
    # f_in = open('B-small-test.in')
    # f_in = open('B-small-attempt1.in')
    f_in = open('B-large.in')
    # f_out = open('B-small.out', 'w')
    f_out = open('B-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        AC, AJ = [int(i) for i in f_in.readline().split()]
        C = []
        D = []
        for _ in range(AC):
            c, d = [int(i) for i in f_in.readline().split()]
            C.append(c)
            D.append(d)
        J = []
        K = []
        for _ in range(AJ):
            j, k = [int(i) for i in f_in.readline().split()]
            J.append(j)
            K.append(k)
        s = solve(AC, AJ, C, D, J, K)
        f_out.write("Case #{}: {}\n".format(t+1, s))
        print "Case #{}: {}\n".format(t+1, s),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
