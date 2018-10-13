from sys import stdin


def compute(N, K):
    acc = [N]
    p = K
    while(p > 0):
        if p == 1:
            acc.sort()
            head = acc.pop()
            if head % 2 == 0:
                return (int(head/2), (int(head/2) - 1))
            else:
                return (int((head - 1)/2), int((head - 1)/2))

        else:
            acc.sort()
            head = acc.pop()
            if head % 2 == 0:
                acc.append(int(head/2))
                acc.append(int(head/2) - 1)
            else:
                acc.append(int((head - 1)/2))
                acc.append(int((head - 1)/2))
        p -= 1
    

T = int(input())

for case in range(1, T+1):
    N, K = list(map(int, stdin.readline().split(' ')))
    y, z = compute(N, K)
    print("Case #{}: {} {}".format(case, y, z))
