answers = []

tests = int(input())

for i in range(tests):
    count = 0

    deck1 = []
    deck2 = []

    a1 = int(input())
    for j in range(4):
        deck1.append(list(map(int, input().split())))

    a2 = int(input())

    for j in range(4):
        deck2.append(list(map(int, input().split())))


    line1 = deck1[a1-1]
    line2 = deck2[a2-1]

    num = 0

    for j in line2:
        if j in line1:
            count += 1
            num = j

    toappend = "Case #" + str(i+1) + ": "
    if count == 0:
        answers.append(toappend + "Volunteer cheated!")
    elif count > 1:
        answers.append(toappend + "Bad magician!")
    else:
        answers.append(toappend + str(num))

[print(x) for x in answers]
