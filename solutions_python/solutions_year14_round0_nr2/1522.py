C = 500.0
F = 4.0
X = 2000.0
base = 2.0


fxs = open("C:\Users\Petr\Downloads\B-large.in", "r")

repeat = int(fxs.readline())

for cnt in range(repeat):

    alpha = fxs.readline().split()
    C = float(alpha[0])
    F = float(alpha[1])
    X = float(alpha[2])


    count = 0
    t = X/base
    t1 = 0.0

    while True:

        t1 += C/(base + F * count)
        count += 1

        if t1 + X/(base + F * count) < t:
            t = t1 + X/(base + count * F)

        else:
            break

    lst = ["Case #", str(cnt + 1), ": ", str(t)]
    print  "".join(lst)
