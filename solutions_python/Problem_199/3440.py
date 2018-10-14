def calculate_answer(S, K):
    S_len = len(S)
    flips = 0
    answer = ''
    all_plus = True
    for i in xrange(S_len):
        if S[i] == '-':
            all_plus = False
            if (S_len - i) >= K:
                k_flag = True
                for k in xrange(i, K + i):
                    if S[k] == '+':
                        k_flag = False
                        S[k] = '-'
                    else:
                        S[k] = '+'
                    all_plus = k_flag
                flips += 1
            else:
                answer = 'IMPOSSIBLE'
                break
    if all_plus:
        answer = str(flips)
    else:
        answer = 'IMPOSSIBLE'
    return answer

in_f = 'A-large.in'
out_f = 'A-large-out.in'
with open(in_f, 'r') as in_file, open(out_f, 'w') as out_file:
    test_cases = int(in_file.readline().strip())
    for t in xrange(1, test_cases + 1):
        s, k = in_file.readline().split(' ')
        S = list(s)
        K = int(k)
        answer = calculate_answer(S, K)
        out_file.write('Case #' + str(t) + ': ' + answer + '\n')
