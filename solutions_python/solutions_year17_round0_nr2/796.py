t = int(input())

for test in range(1, t+1):
    n = [int(i) for i in input()]
    done = False
    while not done:
        done = True
        for i in range(1, len(n)):
            if n[i] < n[i - 1]:
                n[i - 1] -= 1
                for j in range(i, len(n)):
                    n[j] = 9
                done = False

    ans = 0
    for i in range(len(n)):
        ans = ans * 10 + n[i]
    print('Case #%d: %d' % (test, ans))
