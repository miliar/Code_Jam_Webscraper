def pancakes(S, T):
    res = 0
    for i in range(len(S) - T + 1):
        if S[i] is '-':
            res += 1
            for j in range(T):
                if S[i+j] is '-':
                    S[i+j] = '+'
                else:
                    S[i+j] = '-'
    if '-' in S:
        return 'IMPOSSIBLE'
    return str(res)

def main():
    nb_test = int(input())
    for _ in range(nb_test):
        args = input().split()
        print('Case #' + str(_ + 1) + ': ' + pancakes(list(args[0]), int(args[1])))

if __name__ == '__main__':
    main()