with open('A-small-attempt0.in', 'r') as fin:
    T = int(fin.readline())

    for i in range(T):
        row = int(fin.readline())
        for j in range(4):
            if j+1 == row:
                cards = set(fin.readline().split())
            else:
                fin.readline()

        row = int(fin.readline())
        for j in range(4):
            if j+1 == row:
                cards.intersection_update(set(fin.readline().split()))
            else:
                fin.readline()

        if len(cards) > 1:
            result = "Bad magician!"
        elif len(cards) == 0:
            result = "Volunteer cheated!"
        else:
            result = str(list(cards)[0])

        with open('A-small-attempt0.out', 'a') as fout:
            fout.write("Case #%s: %s\n" % (i+1, result))