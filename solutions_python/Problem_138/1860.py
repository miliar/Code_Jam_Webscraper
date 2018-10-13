import sys
sys.setrecursionlimit(10000)

def dec(naomi, ken, score):
    if len(naomi) == 0:
        return score
    elif naomi[0] < ken[0]:
        del naomi[0]
        del ken[len(ken)-1]
        return dec(naomi, ken, score)
    else:
        del naomi[0]
        del ken[0]
        return dec(naomi, ken, score+1)

def war(naomi, ken, score):
    length = len(naomi)
    if length == 0:
        return score
    elif naomi[0] > ken[length-1]:
        return score
    else:
        for i in range(length):
            if ken[i] > naomi[0] :
                del ken[i]
                del naomi[0]
                break
        return war(naomi, ken, score+1)


infile = open(sys.argv[1])
outfile = open("deceitful_war_out", "w")

number = infile.readline().strip()
number = int(number)

for i in range(number):
    blocks = infile.readline().strip()
    blocks = int(blocks)

    naomi = [float(f) for f in infile.readline().split()]
    ken = [float(f) for f in infile.readline().split()]

    naomi = sorted(naomi)
    ken = sorted(ken)

    d_score = dec(naomi[:], ken[:], 0)

    war_score = war(naomi[:], ken[:], 0)

    outfile.write("Case #{0}: {1} {2}\n".format(i+1, d_score, blocks - war_score))
