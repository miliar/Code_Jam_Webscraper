import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
    D, N = [int(i) for i in sys.stdin.readline().split()]

    answer = -1

    for n in range(N):
        K, S = [int(i) for i in sys.stdin.readline().split()]

        cruiseSpeed = (D*S)/(D-K)

        if answer == -1 or cruiseSpeed < answer:
            answer = cruiseSpeed

    print("Case #{}: {}".format(t+1, answer))

