
def solve(N, K):
    # This part ends the recursion
    if K == 1:
        s1 = N // 2
        s2 = N // 2 if N % 2 == 1 else N // 2 -1
        return s1, s2

    # Case A: Everything divides perfectly
    if N % 2 == 1 and K % 2 == 1:
        return solve((N - 1) // 2, (K - 1) // 2)

    # Case B: People divide perfectly stalls do not
    elif K % 2 == 1:
        # I guess the last one will go in the bigger stall section
        return solve(N // 2 - 1, (K - 1) // 2)

    # Case C: Stalls divide perfectly people do not
    elif N % 2 == 1:
        # Does it really matter which section gets which?
        return solve((N - 1) // 2, K // 2)

    # Case D: Nothing divides perfectly
    else:
        # I guess that the big ones will finish last
        return solve(N // 2, K // 2)


if __name__ == "__main__":
    T = int(raw_input())
    for t in range(1, T+1):
        N, K = map(int, raw_input().split())
        print "Case #%d: %d %d" % ((t,) + solve(N, K))
