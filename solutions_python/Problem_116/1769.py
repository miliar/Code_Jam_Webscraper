# Tic-Tac Problem

import sys

x_won = ["XXXT", "TXXX", "XTXX", "XXTX", "XXXX"]
o_won = ["OOOT", "TOOO", "OTOO", "OOTO", "OOOO"]
draw_hint  = "."

def get_match_result(line1, line2, line3, line4):
    draw_chance = 0
    ret_string = "Game has not completed"

    line5  = line1[0]+line2[0]+line3[0]+line4[0]
    line6  = line1[1]+line2[1]+line3[1]+line4[1]
    line7  = line1[2]+line2[2]+line3[2]+line4[2]
    line8  = line1[3]+line2[3]+line3[3]+line4[3]
    line9  = line1[0]+line2[1]+line3[2]+line4[3]
    line10 = line4[0]+line3[1]+line2[2]+line1[3]

    xwon = set(x_won)
    owon = set(o_won)

    # print line1
    # print line2
    # print line3
    # print line4
    # print line5
    # print line6
    # print line7 
    # print line8
    # print line9
    # print line10

    # print x_won
    # print o_won

    x = xwon.intersection([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10])
#    print len(x)
    if len(x) != 0:
        return "X won"

    x = xwon.intersection([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10])
#    print len(x)
    if len(x) != 0:
        return "X won"


    o = owon.intersection([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10])
#    print len(o)
    if len(o) != 0:
        return "O won"

    if "." in line1:
        return ret_string
    if "." in line2:
        return ret_string
    if "." in line3:
        return ret_string
    if "." in line4:
        return ret_string
    if "." in line5:
        return ret_string
    if "." in line6:
        return ret_string
    if "." in line7:
        return ret_string
    if "." in line8:
        return ret_string
    if "." in line9:
        return ret_string
    if "." in line10:
        return ret_string

    return "Draw"     

def compute_results(inbuff, outfd):
    in_cases = int(inbuff[0])
    inbuff = inbuff[1:]
 
    for i in range(0, in_cases):
        j = i * 5

        line1 = inbuff[j].strip()
        line2 = inbuff[j+1].strip()
        line3 = inbuff[j+2].strip()
        line4 = inbuff[j+3].strip()

#        print line1, line2, line3, line4
        result = get_match_result(line1, line2, line3, line4)
        obuffer = "Case #%d: %s\n" %(i+1, result)
        outfd.write(obuffer)

if __name__ == "__main__":
    input = sys.argv[1]
    
    infd = open(input, "r")
    inbuff = infd.readlines()
    
    infd.close()

    outfd = open("output.txt", "w+")
    
    compute_results(inbuff, outfd)
    outfd.close()
    
