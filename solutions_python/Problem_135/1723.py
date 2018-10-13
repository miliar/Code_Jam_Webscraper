t = int(raw_input())

for i in range(1, t + 1):
    r1 = int(raw_input())
    nos1 = []
    for j in range(4):
        temp = raw_input()
        if j + 1 == r1:
            nos1 = temp.split(" ")
    r2 = int(raw_input())
    nos2 = []
    for j in range(4):
        temp = raw_input()
        if j + 1 == r2:
            nos2 = temp.split(" ")
    count = 0
    choice = 0
    answer = ""
    for no in nos1:
        if no in nos2:
            count += 1
            choice = no
    if count == 1:
        answer = str(choice)
    elif count == 0:
        answer = "Volunteer cheated!"
    else:
        answer = "Bad magician!"

    print "Case #" + str(i) + ": " + answer
        
