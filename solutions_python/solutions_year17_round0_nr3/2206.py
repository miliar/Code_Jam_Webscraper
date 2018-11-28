from math import log2, floor

def max_min(N, K):
    period = pow(2, floor(log2(K)))

    maxmin = [0, 0]
    step = 0
    for i in range(K, N + 1):
        if step == period:
            if maxmin[0] == maxmin[1]:
                maxmin[0] += 1
                step = 0
            else:
                maxmin[1] += 1
                step = 0
        step += 1

    return maxmin[0], maxmin[1]

def result():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, K = [int(s) for s in input().split(" ")]
        y, z = max_min(N, K)
        print("Case #{}: {} {}".format(i, y, z))

if __name__ == '__main__':
    result()