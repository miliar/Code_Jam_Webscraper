def solution(D, N, H):
    i=0
    t = 0
    while i < N-1:
        t = max((D - H[i][0]) / H[i][1], t)
        i += 1
    return max((D - H[i][0]) / H[i][1], t)


T = int(input())
for i in range(T):
    D, N = list(map(int, input().split()))
    H = []
    for _ in range(N):
        k, s = list(map(int, input().split()))
        H.append((k, s))
    H = sorted(H, key=lambda x: x[0])
    t = solution(D, N, H)
    print('Case #' +str(i+1)+': '+ str(D/t))
