from __future__ import division

def WP(input_line):
    played = 0
    won = 0
    for letter in input_line:
        if letter == "1":
            won += 1
            played += 1
        if letter == "0":
            played += 1

    ave = won / played
    return ave

def OWP(input_list, play):
    add = 0
    played = 0
    for match in input_list:
        match = list(match)
        if not match[play] == ".":
            played += 1
            del match[play]
            match_string = ""
            for i in match:
                match_string += i
            add += WP(match_string)
    return (add / played)

def OOWP(input_list, team):
    played = 0
    add = 0
    for i in range(len(input_list[team])):
        if not input_list[team][i] == ".":
            OWP_list = input_list[:]
            del OWP_list[i]
            played += 1
            add += OWP(OWP_list, i)
    return (add / played)

def RPI(input_list, team):
    num_WP = WP(input_list[team])
    OWP_list = input_list[:]
    del OWP_list[team]
    num_OWP = OWP(OWP_list, team) 
    num_OOWP = OOWP(input_list, team)
    return 0.25*num_WP + 0.5*num_OWP + 0.25*num_OOWP

in_file = open('in')
out_file = open("out","w")
number_of_tests = int(in_file.readline())
for test_case in range(number_of_tests):
        num_of_teams = in_file.readline()[:-1]
        out_file.write("Case #" + str(test_case + 1) + ":" + "\n")
        input_list = []
        for test_line in range(int(num_of_teams)):
            input_list.append(in_file.readline()[:-1])
        for i in range(int(num_of_teams)):
            out_file.write(str(RPI(input_list,i)) + "\n")
out_file.close()
in_file.close()
