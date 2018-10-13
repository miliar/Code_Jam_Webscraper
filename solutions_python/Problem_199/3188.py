if __name__ == '__main__':
    flipCount = 0
    S = ''
    K = 0

    def flip(n):
        global flipCount
        flipCount += 1
        for r in range(K):
            S[n + r] = '-' if S[n + r] == '+' else '+'
        pass
    testC = input()
    for i in range(int(testC)):
        flipCount = 0
        S = ''
        K = 0
        inputN = str(input())
        S = list(inputN.split(' ')[0])
        K = int(inputN.split(' ')[1])
        if S.count('+') == len(S):
            print("Case #{0}: {1}".format(i + 1, flipCount))
            continue
        while S.count('-') > 0:
            if S.count('+') == len(S):
                print("Case #{0}: {1}".format(i+1, flipCount))
                break
            elif len(S) < K and S.count('-') > 0:
                print("Case #{0}: {1}".format(i+1, 'IMPOSSIBLE'))
                break
            elif S[:len(S)-(K-1)].count('+') == len(S[:len(S)-(K-1)]):
                print("Case #{0}: {1}".format(i+1, 'IMPOSSIBLE'))
                break
            else:
                for i2 in range(len(S)):
                    if i2 <= len(S)-K:
                        sT = []
                        if S[i2] == '-':
                            for i4 in range(K):
                                sT.append(S[i2+i4])
                            if( sT.count('-') == K):
                                flip(i2)
                for i3 in range(len(S) - (K-1)):
                        if S[i3] == '-':
                            flip(i3)

            if S.count('+') == len(S):
                print("Case #{0}: {1}".format(i + 1, flipCount))
                break

