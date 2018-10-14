from sys import stdin

N = int(stdin.readline())

for case_index in xrange(1, N+1):

    answer_one = int(stdin.readline())

    cards_one = []

    for cards_idx in xrange(0,4):
        line = stdin.readline().strip().split(' ')
        row = [int(line[0]),int(line[1]),int(line[2]),int(line[3])]
        cards_one.append(row)

    answer_two = int(stdin.readline())

    cards_two = []

    for cards_idx in xrange(0,4):
        line = stdin.readline().strip().split(' ')
        row = [int(line[0]),int(line[1]),int(line[2]),int(line[3])]
        cards_two.append(row)

    row_one = cards_one[answer_one - 1]
    row_two = cards_two[answer_two - 1]

    intersection = set(row_one).intersection(row_two)

    if len(intersection) == 0 :
        print "Case #" + str(case_index) + ": Volunteer cheated!"
    elif len(intersection) == 1:
        print "Case #" + str(case_index) + ": " + str(intersection.pop())
    else:
        print "Case #" + str(case_index) + ": Bad magician!"
