import logging
import sys

file_name = "A-large"
filein = open("%s.in" % file_name)
fileout = open("%s.out" % file_name, 'w')

def next(list, what, last):
    try:
        another_o = list[last+1:].index(what)
        return another_o + last + 1
    except:
        return -1


def solve(current_case, line):
    if len(line)<2:
        return
    array = line[:-1].split(" ")
    size = int(array[0])
    robots = array[1:][::2]
    buttons = array[1:][1::2]
    next_o = next(robots, "O", -1)
    next_b = next(robots, "B", -1)
    pos_o = 1
    pos_b = 1
    next_button = 0
    num_passo = 1
    while True:

        b_walked = False
        o_walked = False

        if next_b > -1:
             if pos_b != int(buttons[next_b]):
                 direction_b = 1 if pos_b < int(buttons[next_b]) else -1
                 pos_b = pos_b + direction_b
                 b_walked = True

        if next_o > -1:
             if pos_o != int(buttons[next_o]):
                 direction_o = 1 if pos_o < int(buttons[next_o]) else -1
                 pos_o = pos_o + direction_o
                 o_walked = True

        if 1==1:
            if (not b_walked and next_b > -1) and (
                 robots[next_button] == "B"):
                     next_b = next(robots, "B", next_b)
                     next_button = next_button + 1
            elif not o_walked and next_o > -1:
                 if robots[next_button] == "O":
                     next_o = next(robots, "O", next_o)
                     next_button = next_button + 1



        if next_o == -1 and next_b == -1:
            break

        num_passo = num_passo + 1

    fileout.write("Case #%d: %s\n" % (current_case, num_passo))

        
        

def run():

    lines = filein.readlines()
    current_case = 1
    for line in lines[1:]:
        solve(current_case, line)
        current_case = current_case + 1

    filein.close()
    fileout.close()



def main(argv=None):
    if argv is None:
        argv = sys.argv
    #file_name = argv[1]
    run()

if __name__ == "__main__":
    main()
