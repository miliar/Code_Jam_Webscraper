f = open('lottery_input.txt', 'r')

T = int(f.readline())
for case in range(T):
    A, B, K = map(int, f.readline().split())

    count = 0
    for a in range(A):
        for b in range(B):
            if a&b < K:
                count += 1

    print("Case #{0}: {1}".format(case+1, count))

