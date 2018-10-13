def solve(S, K):

    cakes = list(S)

    answer = 0
    for i, c in enumerate(cakes):
        if c == '-':
            answer += 1
            if i + K - 1 < len(cakes):
                for j in range(K):
                    if cakes[i + j] == '-':
                        cakes[i + j] = '+'
                    else:
                        cakes[i + j] = '-'

    if '-' in cakes:
        return "IMPOSSIBLE"
    return answer


if __name__ == '__main__':
    testcases = int(input())

    for nth_case in range(1, testcases + 1):
        N = input().split(" ")

        print("Case #%i: %s" % (nth_case, solve(N[0], int(N[1]))))
