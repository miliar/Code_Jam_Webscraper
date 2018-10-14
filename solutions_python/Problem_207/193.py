
for t in range(int(input())):
    N, R, O, Y, G, B, V = map(int, input().split())

    a = [(R, 'R'), (B, 'B'), (Y, 'Y')]
    a.sort()
    Y, B, R = a

    if R[0]>B[0]+Y[0]:
        print('Case #{}: {}'.format(t+1, 'IMPOSSIBLE'))
        continue

    ans = []
    for i in range(B[0]):
        ans.append(R[1])
        ans.append(B[1])
    for i in range(B[0], R[0]):
        ans.append(R[1])
        ans.append(Y[1])

    ans2 = []
    Y1 = Y[0] - (R[0] - B[0])
    for i in range(len(ans)):
        ans2.append(ans[i])
        if i<Y1:
            ans2.append(Y[1])


    print('Case #{}: {}'.format(t+1, ''.join(ans2)))