T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    arr = []
    while N != 0:
        arr.append(N % 10)
        N /= 10

    z = 0
    for i in xrange(len(arr)-1):
        if arr[i] < arr[i+1]:
            for j in xrange(i+1, len(arr)):
                arr[j] -= 1

                if arr[j] != -1:
                    break

                arr[j] = 9

            arr[i] = 9
            z = i

    for i in range(z):
        arr[i] = 9

    ans = 0
    for i in xrange(len(arr)-1, -1, -1):
        ans *= 10
        ans += arr[i]

    print "Case #" + str(t+1) + ": " + str(ans)

