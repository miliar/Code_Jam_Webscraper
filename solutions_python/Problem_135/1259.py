def cards_in_row(num):
    row = []
    line = ""
    for i in range(1, 5):
        line = raw_input()
        if i == num:
            row = set(line.split(" "))
    return row

i = raw_input()
for j in range(1, int(i)+1):
    num = raw_input()
    first = cards_in_row(int(num))
    num = raw_input()
    second = cards_in_row(int(num))
    inter = first & second
    if len(inter) == 1:
        print "Case #" + str(j) + ": " + inter.pop()
    elif len(inter) == 0:
        print "Case #" + str(j) + ": Volunteer cheated!"
    else:
        print "Case #" + str(j) + ": Bad magician!"
