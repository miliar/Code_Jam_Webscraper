#python 2.7

import sys
import math
import string

def calcRank(R, Y, B):
    ranks = [i[0] for i in sorted(enumerate([R, Y, B]), key=lambda x:x[1], reverse=True)]
    #print [R,Y,B, ranks]
    return ranks

def solve(N, R, Y, B):        
    if R > Y + B or Y > R + B or B > Y + R:
        return "IMPOSSIBLE"
    ret = ""
    last = None
    first = None
    while (R + Y + B > 0):
        ranks = calcRank(R,Y,B)
        if (R == Y == B) and first != None:
            #print "Y" + str(ranks)
            ranks.remove(first)
            if (last == first):
                ranks.insert(1, first)
            else:
                ranks.insert(0, first)
            #print "X" + str(ranks)
        elif (R+Y+B == 2) and first != None:
            #print "Y2" + str(ranks)
            ranks.remove(first)
            if (last == first):
                ranks.insert(1, first)
            else:
                ranks.insert(0, first)
            #print "X2" + str(ranks)
        nextElm = ranks[0]
        if ranks[0] == last:
            nextElm = ranks[1]
        if (nextElm == 0):
            ret += "R"
            assert(R > 0)
            R -= 1
        if (nextElm == 1):
            ret += "Y"
            assert(Y > 0)
            Y -= 1
        if (nextElm == 2):
            ret += "B"
            assert(B > 0)
            B -= 1
        last = nextElm
        if (first == None):
            first = nextElm
    print ret
    assert(ret[0] != ret[-1])
    lastChar = None
    firstChar = None
    for i in range(0,len(ret)):
        if (firstChar == None):
            lastChar = ret[i]
            firstChar = ret[i]
        else:
            assert(lastChar != ret[i])
            lastChar = ret[i]

    assert(lastChar != firstChar)
    return ret

def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    for i in range(0,case_count):
        #print split_input[i+1]
        N, R, O, Y, G, B, V = split_input[i+1].split(" ")
        res = solve(int(N), int(R), int(Y), int(B))
        print "Case #" + str(i+1) + ": " + str(res)
        output_file.write("Case #" + str(i+1) + ": " + str(res) + "\n")
    
if __name__ == "__main__":
    main()
