T = int(input())
outfile = open('out.txt', 'w+')

for case in range(1, T + 1):
    S, K = input().split()
    K = int(K)

    flips = 0
    i = 0
    j = len(S) - K

    def flip(s):
        return ''.join(['-' if x == '+' else '+' for x in s])

    print('case', case)
    print(S)
    print(' ' * i, 'i', ' ' * (j - i - 1), 'j', sep='')
    while(i <= j):
        if(S[i] == '-'):
            S = S[:i] + flip(S[i:i+K]) + S[i+K:] 
            flips += 1
            print(S)
            print(' ' * i, 'i', ' ' * (j - i - 1), 'j', sep='')

        if(S[j+K-1] == '-'):
            S = S[:j] + flip(S[j:j+K]) + S[j+K:] 
            flips += 1
            print(S)
            print(' ' * i, 'i', ' ' * (j - i - 1), 'j', sep='')
        i += 1
        j -= 1
    print(flips, 'flips')
    print('~' * 80)
    outfile.write('Case #' + str(case) + ': ' + 
                    (str(flips) if '-' not in S else 'IMPOSSIBLE') + '\n')
