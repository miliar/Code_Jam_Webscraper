TT = int(input())
for T in range(1, TT+1):
    N, R, O, Y, G, B, V = map(int, input().split())
    values = [[R, 'R'], [Y, 'Y'], [B, 'B']]
    values.sort(reverse=True)
    if values[0][0] > N // 2:
        print(f'Case #{T}: IMPOSSIBLE')
        continue
    S = []
    for i in range(values[0][0]):
        S.append(values[0][1])
    res = values[1][1] * values[1][0] + values[2][1] * values[2][0]
    for i in range(len(res)):
        S[i % len(S)] += res[i]
    S = ''.join(S)
    print(f'Case #{T}: {S}')
