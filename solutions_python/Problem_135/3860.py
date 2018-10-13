fin = open("A-small-attempt0.in")
fout = open("output.txt", 'w')
lines = []
row = []
card_rows = []
cards = []
for line in fin:
    line = line.strip()
    lines.append(line)
row = []
for i in range(int(lines[0])*2):
    row = lines[1+int(lines[1])].split()
    print(row)
    card_rows.append(row)
    for i in range(1, 6):
        lines.remove(lines[1])
    row = []
print(card_rows)
for i in range(0, len(card_rows), 2):
    for card1 in card_rows[i]:
        for card2 in card_rows[i+1]:
            if card1 == card2:
                cards.append(card1)
    if len(cards) == 1:
        fout.write("Case #" + str(int(i/2+1)) + ": " + cards[0] + "\n")
    elif len(cards) > 1:
        fout.write("Case #" + str(int(i/2+1)) + ": " + "Bad magician!\n")
    else:
        fout.write("Case #" + str(int(i/2+1)) + ": " + "Volunteer cheated!\n")
    cards = []
fin.close()
fout.close()
