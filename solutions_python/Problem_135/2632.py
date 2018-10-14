import sys
f = open("A-small-attempt1.in")
o = open("A-small-attempt1.out", "w")
T = int(f.readline())
for t in range(T):

    rows = []
    guess1 = int(f.readline())
    for ii in range(4):
        rows.append(f.readline().split(" "))
    possibles = []
    for element in rows[guess1-1]:
        possibles.append(int(element))

    rows = []
    guess2 = int(f.readline())
    for ii in range(4):
        rows.append(f.readline().split(" "))

    possibles2 = []
    for element in rows[guess2-1]:
        possibles2.append(int(element))

    count = 0
    ans = 0
    for number in possibles:
        if number in possibles2:
            ans = number
            count += 1
    if count == 1:
        o.write("Case #"+str(t+1)+": "+ str(ans) + "\n")
    elif count == 0:
        o.write("Case #"+str(t+1)+": "+ "Volunteer cheated!"+ "\n")
    else:
        o.write("Case #"+str(t+1)+": "+ "Bad magician!"+ "\n")

    #f.readline()