def solve(S_max, S):
    standing = 0
    invite = 0
    for i, s in enumerate(S):
        if standing < i:
            invite += i-standing
            standing = i
        if standing >= i:
            standing += s
    return invite


if __name__ == '__main__':
    T = int(input())
    for case in range(1, T+1):
        S_max, S = input().split()
        S = [int(i) for i in list(S)]
        print("Case #%d: %d" % (case, solve(S_max, S)))

