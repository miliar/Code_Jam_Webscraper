f = open("input", "r")
o = open("output", "w")

t = int(f.readline())

for test in range(t):
    row1 = int(f.readline()) - 1
    cards1 = []
    for i in range(4):
        cards1.append([int(x) for x in f.readline().split(" ")])

    row2 = int(f.readline()) - 1
    cards2 = []
    for i in range(4):
        cards2.append([int(x) for x in f.readline().split(" ")])

    cards = list(set(cards1[row1]) & set(cards2[row2]))
    answer = "Bad magician!" if len(cards) > 1 else "Volunteer cheated!" if len(cards) < 1 else str(cards[0])

    o.write("Case #%d: %s\n" % (test+1, answer))

f.close()
o.close()
