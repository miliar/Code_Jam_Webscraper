from copy import copy

cases = int(input())

for i in range(cases):
    blocks = int(input())
    N = input().strip('\n').split(' ')
    K = input().strip('\n').split(' ')
    for j in range(blocks):
        N[j] = float(N[j])
        K[j] = float(K[j])
    Nh = copy(N)
    Kh = copy(K)

    # Deceitful War
    countN = 0
    countK = 0
    countNh = 0
    countKh = 0
    while (len(N)):
        if (min(N) < min(K)):
            N.pop(N.index(min(N)))
            K.pop(K.index(max(K)))
            countK += 1
        else:
            N.pop(N.index(min(N)))
            K.pop(K.index(min(K)))
            countN += 1
    while (len(Nh)):
        if (max(Kh) > max(Nh)):
            Nh.pop(Nh.index(max(Nh)))
            Kh.pop(Kh.index(max(Kh)))
            countKh += 1
        else:
            Nh.pop(Nh.index(max(Nh)))
            Kh.pop(Kh.index(min(Kh)))
            countNh += 1

    print("Case #" + str(i + 1) + ": " + str(countN) + " " + str(countNh))
