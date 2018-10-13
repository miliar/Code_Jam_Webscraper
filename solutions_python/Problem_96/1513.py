fin = open("3.in")
fout = open("3.out", "w")

T = int(fin.readline())

for i in range(T):
    scores = [int(j) for j in fin.readline().strip().split()]
    N = scores.pop(0)
    S = scores.pop(0)
    p = scores.pop(0)
    count = 0

    for k in scores: 
        base = k / 3
        triplet = [base] * 3
        remainder = k % 3

        target = base

        if (target >= p):
            count += 1
            continue

        if (remainder == 0):
            if (p - target <= 1 and S > 0 and base > 0):
                count += 1
                S -= 1
                continue

        if (remainder == 1):
            if (p - target <= 1):
                count += 1
                continue

        if (remainder == 2):
            if (p - target <= 1):
                count += 1
                continue
            elif (p - target <= 2 and S > 0):
                count += 1
                S -= 1
                continue

    fout.write("Case #" + str(i + 1) + ": " + str(count) + "\n");
    print count

fout.close()
fin.close()
