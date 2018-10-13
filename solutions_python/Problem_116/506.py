import sys

file = open(sys.argv[1])
case = int(file.readline())

x_won = "X won"
o_won = "O won"
draw = "Draw"
not_finished = "Game has not completed"
line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
cow_1 = ""
cow_2 = ""
cow_3 = ""
cow_4 = ""
diag_1 = ""
diag_2 = ""


def test_line(player, line):
        nb_played = 0
        nb_T = 0
        ok = 0
        for i in line:
                if i == player:
                        nb_played += 1
                elif i == "T":
                        nb_T += 1

        if nb_played == 4 or (nb_played == 3 and nb_T == 1):
                ok = 1

        return ok

def test_player(player):
        result = test_line(player, line_1)
        result |= test_line(player, line_2)
        result |= test_line(player, line_3)
        result |= test_line(player, line_4)
        result |= test_line(player, cow_1)
        result |= test_line(player, cow_2)
        result |= test_line(player, cow_3)
        result |= test_line(player, cow_4)
        result |= test_line(player, diag_1)
        result |= test_line(player, diag_2)

        if result:
                return 1
        else:
                return 0

def found_empty_slot(): 
        find = 0
        for line in line_1, line_2, line_3, line_4:
                for i in range(4):
                        if line[i] == ".":
                                return 1

        return 0


for i in range(case):
        find = 0
        line_1 = list(file.readline())
        line_2 = list(file.readline())
        line_3 = list(file.readline())
        line_4 = list(file.readline())
        cow_1 = line_1[0] + line_2[0] + line_3[0] + line_4[0]
        cow_2 = line_1[1] + line_2[1] + line_3[1] + line_4[1]
        cow_3 = line_1[2] + line_2[2] + line_3[2] + line_4[2]
        cow_4 = line_1[3] + line_2[3] + line_3[3] + line_4[3]
        diag_1 = line_1[0] + line_2[1] + line_3[2] + line_4[3]
        diag_2 = line_1[3] + line_2[2] + line_3[1] + line_4[0]

        result = test_player("X")
        if result == 1:
                print "Case #%d: %s" % (i+1, x_won)
                find = 1
        else:
                result = test_player("O")
                if result == 1:
                        print "Case #%d: %s" % (i+1, o_won)
                        find = 1
        
        if find == 0:
                if found_empty_slot():
                        print "Case #%d: %s" % (i+1, not_finished)
                else:
                        print "Case #%d: %s" % (i+1, draw)

        # Reading the empty line
        file.readline()

