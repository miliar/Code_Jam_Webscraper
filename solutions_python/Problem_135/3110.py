import string

f = open('testcase', 'r')
num_cases = int(string.strip(f.readline()))

for i in xrange(num_cases):
    ok_cards = []
    first_row = int(string.strip(f.readline()))
    first_board = [[int(k) for k in string.split(string.strip(f.readline()), ' ')] for j in xrange(4)]
    first_cards = first_board[first_row-1]
    second_row = int(string.strip(f.readline()))
    second_board = [[int(k) for k in string.split(string.strip(f.readline()), ' ')] for j in xrange(4)]
    second_cards = second_board[second_row-1]
    for x in first_cards:
        if x in second_cards:
            ok_cards.append(x)
    if len(ok_cards) == 0:
        print "Case #"+str(i+1)+": Volunteer cheated!"
    elif len(ok_cards) == 1:
        print "Case #"+str(i+1)+": "+str(ok_cards[0])
    else:
        print "Case #"+str(i+1)+": Bad magician!"
