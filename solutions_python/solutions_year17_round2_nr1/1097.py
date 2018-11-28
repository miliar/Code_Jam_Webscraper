def solve(D, hs):
    return D / max((D - K) / S for K, S in hs if K < D)

# solve(2525, [[2400, 5]])
# solve(300, [[120, 60], [60, 90]])
# solve(100, [[80, 100], [70, 10]])
#%%

def main():
    T = int(input())
    for i in range(1, 1 + T):
        D, N = map(int, input().split())
        horses = [list(map(int, input().split())) for _ in range(N)]
        print('Case #{}: {}'.format(i, solve(D, horses)))

if __name__ == '__main__':
    main()
