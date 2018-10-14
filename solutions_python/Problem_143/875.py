def solve(A, B, K):
    count = 0
    for i in range(A):
        for j in range(B):
            if i&j < K:
                count += 1

    return count

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(T):
        A, B, K = [int(x) for x in raw_input().split()]
        ret = solve(A, B, K)
        print "Case #{}: {}".format(i+1, ret)
