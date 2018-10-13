def main():
    T = int(input())
    for t in range(1, T + 1):
        S, K = input().split()
        K = int(K)
        ret = 0
        arr = [c for c in S]
        for i, a in enumerate(arr):
            if a == '-' and i + K <= len(S):
                ret += 1
                for j in range(i, i + K):
                    arr[j] = '+' if arr[j] == '-' else '-'
        ret = "IMPOSSIBLE" if '-' in arr else str(ret)
        print("Case #{t}: {ret}".format(t=t, ret=ret))

if __name__ == '__main__':
    main()
