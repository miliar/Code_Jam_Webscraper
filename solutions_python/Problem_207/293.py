T = int(raw_input())

for t in xrange(T):
    N, R, O, Y, G, B, V = map(int, raw_input().split())

    arr = [[R, 'R'], [Y, 'Y'], [B, 'B']]
    arr.sort(reverse=True)

    if arr[0][0] > N/2:
        print "Case #" + str(t + 1) + ": " + "IMPOSSIBLE"
    else:
        ans = [''] * N
        x = N / arr[0][0]
        i = 0
        while arr[0][0] != 0:
            ans[x*i] = arr[0][1]
            arr[0][0] -= 1
            i += 1

        for i in xrange(N):
            if ans[i] == '':
                if arr[1][0] > arr[2][0]:
                    if arr[1][0] > 0 and ans[i-1] != arr[1][1] and ans[(i+1)%N] != arr[1][1]:
                        ans[i] = arr[1][1]
                        arr[1][0] -= 1
                    else:
                        ans[i] = arr[2][1]
                        arr[2][0] -= 1
                else:
                    if arr[2][0] > 0 and ans[i-1] != arr[2][1] and ans[(i+1)%N] != arr[2][1]:
                        ans[i] = arr[2][1]
                        arr[2][0] -= 1
                    else:
                        ans[i] = arr[1][1]
                        arr[1][0] -= 1

        print "Case #" + str(t + 1) + ": " + ''.join(ans)
