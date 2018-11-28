stuff = []


with open("b.in", "r") as txt:
    for line in txt:
        lis = line.strip('\n')
        stuff += [lis]

lines = int(stuff[0])

for i in range (1, lines+1):
    args = stuff[i].split()
    C = float(args[0]) # farm cost
    F = float(args[1]) # farm bonus
    X = float(args[2]) # win
    N = 1 # number of farms
    TF = C/2 
    T1 = X/2 # time taken
    T2 = 0
    while (True):
        T2 = TF + X/(2+(N*F))
        if (T2 > T1):
            break
        else:
            TF += C/(2+(N*F))
            T1 = T2
            N += 1
    print("Case #" + str(i) + ": %.7f" % T1)
