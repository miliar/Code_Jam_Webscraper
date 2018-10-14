import sys
T = input()

for t in range(T):
    answer1 = input()
    for i in range(answer1-1):
        raw_input()
    row1 = raw_input().split(' ')
    for i in range(4-answer1):
        raw_input()


    answer2 = input()
    for i in range(answer2-1):
        raw_input()
    row2 = raw_input().split(' ')
    for i in range(4-answer2):
        raw_input()

    matches = []
    for x in row1:
        if x in row2:
            matches.append(x)

    sys.stdout.write ("Case #%d: " % (t+1,))
    if len(matches) == 0:
        print "Volunteer cheated!"
    elif len(matches) == 1:
        print matches[0]
    else:
        print "Bad magician!"
