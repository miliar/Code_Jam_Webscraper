import sys
import re

stdin = list(sys.stdin)

for i, scenario in enumerate(stdin[1:]):
    moves =  re.findall('[BO]', scenario.rstrip("\n")[2:])

    blue_moves = [int(element) for element in re.findall('(?<=B )\d+', scenario.rstrip("\n")[2:])]
    orange_moves = [int(element) for element in re.findall('(?<=O )\d+', scenario.rstrip("\n")[2:])]
    orange = 1
    blue = 1

    # print moves
    # print blue_moves
    # print orange_moves
    # print "++++++++++++++"

    moves.reverse()
    blue_moves.reverse()
    orange_moves.reverse()

    timer = True;
    sec = 0;

    next_push = moves.pop()
    if blue_moves:
        next_blue_move = blue_moves.pop()
    else:
        next_blue_move = 1
    if orange_moves:
        next_orange_move = orange_moves.pop()
    else:
        next_orange_move = 1

    while True:
        sec+=1;

        orange_move_allowed = True
        blue_move_allowed = True

        # print "Time: %s" % sec,
        if next_push == "O":
            if orange == next_orange_move:
                # print "Orange pushes button: %s  " % orange,
                if moves:
                    next_push = moves.pop()
                else:
                    break
                if orange_moves:
                    orange_move_allowed = False
                    next_orange_move = orange_moves.pop()
        else:
            if next_push == "B":
                if blue == next_blue_move:
                    # print "Blue pushes button: %s  " % orange,
                    if moves:
                        next_push = moves.pop()
                    else:
                        break
                    if blue_moves:
                        blue_move_allowed = False
                        next_blue_move = blue_moves.pop()

        if orange_move_allowed and next_orange_move != orange:
            if next_orange_move > orange:
                orange+=1
            else:
                orange-=1
            # print "Orange moves to the button: %s  " % orange,
        else:
            pass
            # print "Orange stays on the button: %s  " % orange,

        if blue_move_allowed and next_blue_move != blue:
            if next_blue_move > blue:
                blue+=1
            else:
                blue-=1
            # print "Blue moves to the button: %s  " % blue,
        else:
            pass
            # print "Blue stays on the button: %s" % blue,

        # print " "
        # print next_push,"+"
        # print next_blue_move
        # print next_orange_move


    print "Case #%s: %s" % (i+1, sec)

    # for move in moves:
    #     if move[0] == "O":
    #         print "push", move[0], orange
    #         if orange != move[2]:
    #             pass

    #     if move[0] == "B":
    #         print "push", move[0], blue
