blockNum = 9
blockNaomi = [0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]
blockKen = [0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458]
repeat = 1

fxs = open("C:\Users\Petr\Downloads\D-large.in", "r")
repeat = int(fxs.readline())

for count in range(repeat):
    blockNum = int(fxs.readline())
    blockNaomi = fxs.readline().split()[:]
    blockKen = fxs.readline().split()[:]

    blockNaomi.sort()
    blockKen.sort()
    pointsNaomi = 0
    pointsKen = 0

    blockNaomiC = blockNaomi[:]
    blockKenC = blockKen[:]
    pointsNaomiC = 0
    pointsKenC = 0

    while len(blockNaomi) > 0:
        if blockNaomi[-1] > blockKen[-1]:
            del blockNaomi[-1]
            del blockKen[-1]
            pointsNaomi += 1
        elif blockNaomi[0] > blockKen[-1]:
            pointsNaomi += len(blockNaomi)
            break
        else:
            del blockNaomi[0]
            del blockKen[-1]
            pointsKen += 1

    while len(blockNaomiC) > 0:
        if blockNaomiC[-1] > blockKenC[-1]:
            pointsNaomiC += 1
            del blockNaomiC[-1]
            del blockKenC[0]
        else:
            pointsKenC += 1
            del blockNaomiC[-1]
            del blockKenC[-1]


    lst = ["Case #", str(count + 1), ": ", str(pointsNaomi), " ", str(pointsNaomiC)]
    print  "".join(lst)
