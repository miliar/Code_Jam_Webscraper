def main():
    T = int(raw_input().strip())
    for count in xrange(1, T + 1):
        S, K = raw_input().strip().split(' ')
        K = int(K)
        S = list(S)
        len_S = len(S)
        left_most_blank = 0
        ans = 0
        side = {'+': '-', '-': '+'}
        i = left_most_blank
        for i in xrange(left_most_blank, len_S - K + 1):
            if S[i] == '-':
                break
        left_most_blank = i
        while 1:
            if left_most_blank == len_S - K:
                if S.count('-') == K:
                    ans += 1
                elif S.count('-') > 0 and S.count('+') > 0 and K > 1:
                    ans = -1
                break
            for i in xrange(left_most_blank, left_most_blank + K):
                S[i] = side[S[i]]
            ans += 1
            i = left_most_blank
            for i in xrange(left_most_blank, len_S - K + 1):
                if S[i] == '-':
                    break
            left_most_blank = i
        if ans >= 0:
            print 'Case #' + str(count) + ': ' + str(ans)
        else:
            print 'Case #' + str(count) + ': IMPOSSIBLE'


if __name__ == '__main__':
    main()
