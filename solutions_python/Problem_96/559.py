num_rows = raw_input()

for i in range(int(num_rows)):
    line = raw_input()
    ar = line.split(" ")
    n = int(ar[0])
    s = int(ar[1])
    p = int(ar[2])

    scores = []
    for j in range(n):
        scores.append(int(ar[j+3]))

    counter = 0
    for j in range(n):
        if p == 0:
            counter = counter + 1
        elif p == 1:
            if scores[j] == 0:
                1
            else:
                counter = counter + 1
        else:
            no_surprise_min = p*3-2
            surprise = p*3-4
            if scores[j] >= no_surprise_min:
                counter = counter + 1
            elif scores[j] >= surprise:
                if s > 0:
                    counter = counter + 1
                    s = s - 1
                else:
                    1
            else:
                1

    print "Case #" + str(i+1) + ": " + str(counter)

