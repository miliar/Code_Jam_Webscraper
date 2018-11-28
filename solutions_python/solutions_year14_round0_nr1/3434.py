f = open("file.txt")
for i in range(int(f.readline())):
    a1 = int(f.readline())
    set1 = []
    for line in range(4):
        set1.append([int(x) for x in f.readline().split(" ")])
    selectedRow1 = set1[a1-1]
    a2 = int(f.readline())
    set2 = []
    for line in range(4):
        set2.append([int(x) for x in f.readline().split(" ")])
    selectedRow2 = set2[a2-1]
    cards = []

    for card in selectedRow1:
        if (card in selectedRow2): cards.append(card)
    a = open("out.txt", 'a')
    ans = ""
    if (len(cards) == 0) : ans = "Volunteer cheated!"
    elif(len(cards) > 1) : ans = "Bad magician!"
    else: ans = cards[0]
    a.write("Case #%i: %s" %(i+1, str(ans) + "\n"))
    a.close()
f.close()
