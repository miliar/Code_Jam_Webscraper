fin = open("A.in", "r")

T = int(fin.readline())

for i in range(T):
    rown = int(fin.readline())
    for l in range(4):
        r = fin.readline()
        if l + 1 == rown:
            row = [int(a) for a in r.split()]
    
    coln = int(fin.readline())
    for l in range(4):
        c = fin.readline()
        if l + 1 == coln:
            col = [int(a) for a in c.split()]

    cards = list(set(row) & set(col))

    if len(cards) == 0:
        answer = "Volunteer cheated!"
    elif len(cards) == 1:
        answer = str(cards[0])
    else:
        answer = "Bad magician!"

    print("Case #" + str(i + 1) + ": " + answer)

