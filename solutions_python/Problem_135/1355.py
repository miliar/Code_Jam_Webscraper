#!/usr/bin/python3.2

filename = "A-small-attempt0.in"

FILE = open(filename)
T = int(FILE.readline())

for i in range(1,T+1):
    answer_a = int(FILE.readline()[0])
    arrange_a = []
    arrange_a.append(FILE.readline().split())
    arrange_a.append(FILE.readline().split())
    arrange_a.append(FILE.readline().split())
    arrange_a.append(FILE.readline().split())

    answer_b = int(FILE.readline()[0])
    arrange_b = []
    arrange_b.append(FILE.readline().split())
    arrange_b.append(FILE.readline().split())
    arrange_b.append(FILE.readline().split())
    arrange_b.append(FILE.readline().split())

    potential_a = set( arrange_a[answer_a - 1] )
    potential_b = set( arrange_b[answer_b - 1] )

    potential = potential_a & potential_b

    if len(potential) == 0:
        out = "Volunteer cheated!"
    elif len(potential) == 1:
        out = list(potential)[0]
    else:
        out = "Bad magician!"




    print('Case #' + str(i) + ': ' + out)
