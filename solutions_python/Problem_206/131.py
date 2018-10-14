if __name__ == '__main__':
    T = int(raw_input())
    for t in range(1, T+1):
        D, N = map(int, raw_input().split())
        max_time = 0
        for i in range(N):
            K, S = map(int, raw_input().split())
            time = float(D - K) / S
            max_time = time if time > max_time else max_time
        spd = float(D) / max_time
        print 'Case #{}: {}'.format(t, spd)

