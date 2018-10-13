def solve(N, A):
    swaps, high = 0, N
    m = max(A)
    for rep in range(N - 1):
        mini, minv = 0, m
        for i in range(high):
            if A[i] < minv:
                mini, minv = i, A[i]
        swaps += min(mini, high - mini - 1)
        A.pop(mini)
        high -= 1
    return swaps

def main():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        As = [int(a) for a in input().split()]
        res = solve(N, As)
        print('Case #', i, ': ', res, sep='')

if __name__ == "__main__":
    main()
