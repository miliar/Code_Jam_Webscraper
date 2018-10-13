import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
    line = sys.stdin.readline().strip().split()
    S = int(line[0])
    histogram = [int(x) for x in line[1]]
    cumsum = [0] * len(histogram)
    for i in range(len(histogram)):
        cumsum[i] = cumsum[i-1] + histogram[i] if i > 0 else histogram[i]

    #print(histogram, cumsum)
    added = 0
    for s in range(1, len(histogram)):
        if histogram[s] == 0:
            continue
        diff = s - cumsum[s-1] - added
        if diff > 0:
            added += diff

    print("Case #{}: {}".format(t+1, added))

