from copy import deepcopy

def run_test(case):
    D, N = map(int, input().split())
    H = []
    for i in range(N):
        K, S = map(int, input().split())
        dist = D - K
        time = dist / S
        H.append(time)
    maxTime = max(H)
    maxSpeed = D / maxTime
    print("Case #{}: {:.6f}".format(case, maxSpeed))

def printGrid(x):
    for i in x:
        s = ""
        for c in i:
            s += c  + ""
        print(s)

for i in range(1, int(input()) + 1):
    run_test(i)
