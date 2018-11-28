def calc_war(blocks, naomi, ken):
    score = blocks
    used = []
    for n in range(0, blocks):
        for k in range(0, blocks):
            if ken[k] > naomi[n] and ken[k] not in used:
                score -= 1
                used.append(ken[k])
                break
    return score
                

def calc_deceit(blocks, naomi, ken):
    score = 0
    n = 0
    k = 0
    while n != blocks:
        if naomi[n] < ken[k]:
            n += 1
        else:
            score += 1
            n += 1
            k += 1
    return score

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
input = args.input
output = args.output
print "Reading input file", input

inputfile = open(input, "r")
outputfile = open(output, "w")

cases = int(inputfile.readline())
print "There are", cases, "test cases"

for x in range(0, cases):
    blocks = int(inputfile.readline())
    naomi = sorted(map(float, inputfile.readline().split()))
    ken = sorted(map(float, inputfile.readline().split()))

    war = calc_war(blocks, naomi, ken)
    deceit = calc_deceit(blocks, naomi, ken)

    outputfile.write("Case #" + str(x + 1) + ": ")
    outputfile.write(str(deceit))
    outputfile.write(" ")
    outputfile.write(str(war))
    outputfile.write("\n")

inputfile.close()
outputfile.close()
