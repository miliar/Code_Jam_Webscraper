#### Problem A. Magic Trick ####

# from math import sqrt, ceil, floor


# input
filename = "input"
lines = (line.rstrip('\n') for line in open(filename))
T = int(lines.__next__())

# output
output = open('output', 'w+')

# test case loop
for caseIdx in range(T):

    a1 = int(lines.__next__())
    sq1 = []
    for _ in range(4):
        row = map(int, lines.__next__().split(' '))
        sq1.append(row)

    a2 = int(lines.__next__())
    sq2 = []
    for _ in range(4):
        row = map(int, lines.__next__().split(' '))
        sq2.append(row)

    candidates = set(sq1[a1-1]).intersection(sq2[a2-1])
    if len(candidates) == 0:
        msg = 'Volunteer cheated!'
    elif len(candidates) == 1:
        msg = str(candidates.pop())
    else:
        msg = 'Bad magician!'


    # print output
    out = 'Case #' + str(caseIdx + 1) + ': ' + msg + '\n'
    output.write(out)

output.close()
print(open('output', 'r').read())
