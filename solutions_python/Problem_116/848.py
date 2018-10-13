
def check(instr):
    if instr.replace("T", "X").count("X") == 4:
        return "X"
    elif instr.replace("T", "O").count("O") == 4:
        return "O"
    return "."

import sys

T = int(sys.stdin.readline())

for i in xrange(T):
    input = sys.stdin.readline().strip()
    input += sys.stdin.readline().strip()
    input += sys.stdin.readline().strip()
    input += sys.stdin.readline().strip()

    all_input = [
    input[0:4],
    input[4:8],
    input[8:12],
    input[12:16],
    input[0:16:4],
    input[1:16:4],
    input[2:16:4],
    input[3:16:4],
    input[0:16:5],
    input[3:15:3]]

    for foo in all_input:
        #print foo
        bar = check(foo)
        if bar == "X":
            print "Case #%d: %s" % (i+1, "X won")
            break
        elif bar == "O":
            print "Case #%d: %s" % (i+1, "O won")
            break

    if bar == ".":
        if "." in input:
            print "Case #%d: %s" % (i+1, "Game has not completed")
        else:
            print "Case #%d: %s" % (i+1, "Draw")

    sys.stdin.readline()
