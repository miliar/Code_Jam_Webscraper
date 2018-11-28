import sys

sys.stdin = open('C-small-1-attempt0.in', 'r')
sys.stdout = open('C-small.out', 'w')


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, K = [int(s) for s in input().split(" ")]
    l1 = []
    l1.append(N)
    while K > 1:
        max = 0
        for rec in l1:
            if rec > max:
                max = rec
        l1[l1.index(max)] = -1;
        if max % 2 == 0:
            l1.append((max - 2) / 2)
            l1.append(max / 2)
        else:
            tmp = (max - 1) / 2
            l1.append(tmp)
            l1.append(tmp)
        K -= 1
    # compute maxdist and mindist for last person
    max = 0
    for rec in l1:
        if rec > max:
            max = rec
    if max % 2 == 0:
        mindist = ((max - 2) / 2)
        maxdist = (max / 2)
    else:
        mindist = ((max - 1) / 2)
        maxdist = mindist
    print("Case #{}: {} {}".format(i, int(maxdist), int(mindist)))
