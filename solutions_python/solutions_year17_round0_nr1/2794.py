def change_pancake_side(l):
    if l == '+':
        return('-')
    else:
        return('+')

with open('A-small-attempt0.in.txt') as input_file:
    T = int(input_file.readline())
    for number_test in range(T):
        use_flipper = 0
        S, K = input_file.readline().split()
        S = list(S)
        K = int(K)
        i = 0
        while i + K <= len(S):
            if S[i] == '-':
                for j in range(K):
                    S[i+j] = change_pancake_side(S[i+j])
                use_flipper += 1
            i +=1
        if '-' in S[-K:]:
            print('Case #' + str(number_test+1) +': ' + 'IMPOSSIBLE')
        else:
            print('Case #' + str(number_test+1) +': ' + str(use_flipper))