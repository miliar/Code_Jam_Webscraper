def flip(S, K, index):
    return S[:index] + S[index:index + K].translate(str.maketrans("+-", "-+")) + S[index + K:]


def solve(S, K):
    flips = 0
    for i in range(len(S) - K + 1):
        if S[i] == '-':
            S = flip(S, K, i)
            flips += 1
    if '-' in S:
        return "IMPOSSIBLE"
    return flips


def main():
    T = int(input())
    for case in range(T):
        line = input()
        S = line.split()[0]
        K = int(line.split()[1])
        answer = solve(S, K)
        print("Case #{}: {}".format(case + 1, answer))


if __name__ == '__main__':
    main()
