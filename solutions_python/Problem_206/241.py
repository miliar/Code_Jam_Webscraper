
def cruise_control(D, horses):
    t = max((D - k) / s for k, s in horses)
    return D / t

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        D, N = map(int, input().split())
        horses = []
        for j in range(N):
            K, S = map(int, input().split())
            horses.append((K, S))
        result = cruise_control(D, horses)
        print("Case #{}: {}".format(i + 1, result))
