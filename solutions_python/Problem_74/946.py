def solve(input):
    split = input.split(' ')
    moves = zip(split[1::2], split[2::2])

    oloc = 1
    bloc = 1
    time = 0
    omoves = [(x, y) for x, y in moves if x=='O']
    bmoves = [(x, y) for x, y in moves if x=='B']

    while moves:
        time = time + 1
#        print "Turn %d" % time
        pushed = False
        if omoves:
            # figure out where o needs to be for its next action
            # if it's already there, either take it or stay put
            (_, move_loc) = omoves[0]
            move_loc = int(move_loc)
            if move_loc == oloc:
                # if this is the top move on stack, do it, otherwise stay
                if moves[0][0] == 'O':
#                    print "O pushed button %d" % oloc
                    pushed = True
                    omoves.pop(0)
                    moves.pop(0)
                else:
#                    print "O stayed at %d" % oloc
                    pass
            else:
                # move!
                oloc = oloc + (1 if move_loc > oloc else -1)
#                print "O moved to %d.. seeking %d" % (oloc, move_loc)
        if bmoves:
            # figure out where b needs to be for its next action
            # if it's already there, either take it or stay put
            (_, move_loc) = bmoves[0]
            move_loc = int(move_loc)
            if move_loc == bloc:
                # if this is the top move on stack, do it, otherwise stay
                if moves[0][0] == 'B' and not pushed:
 #                   print "B pushed button %d" % bloc
                    pushed = True
                    bmoves.pop(0)
                    moves.pop(0)
                else:
 #                    print "B stayed at %d" % bloc
                    pass
            else:
                # move!
                bloc = bloc + (1 if move_loc > bloc else -1)
#                print "O moved to %d.. seeking %d" % (bloc, move_loc)

    
    return time
        

test1 = "4 O 2 B 1 B 2 O 4"
test2 = "3 O 5 O 8 B 100"


def runcase(num, f):
    line = f.readline().strip()
    print "Case #%d: %d" % (num, solve(line))

f = open('A-large.in')

cases = int(f.readline())

for case in range(1, cases+1):
    runcase(case, f)
