#!/env/python
def get_answer(infile):
    a = int(infile.readline())
    for row in xrange(4):
        curr_row_str = infile.readline()
        if row == a-1:
            a_row = [int(x) for x in curr_row_str.split()]
    return a, a_row

if __name__ == "__main__":
    infile = open("./data/A-small-attempt0.in", 'r')
    outfile = open("./data/A-small-attempt0.out", 'w')
    n = int(infile.readline())
    for c in xrange(n):
        a_1, a_1_row = get_answer(infile)
        a_2, a_2_row = get_answer(infile)
        poss = []
        for card_n in a_1_row:
            if card_n in a_2_row:
                poss.append(card_n)

        if len(poss) == 0:
            print("cheat")
            outfile.write("Case #{cn}: Volunteer cheated!\n".format(cn=c+1))
        if len(poss) == 1:
            print "answer: {}".format(poss[0])
            outfile.write("Case #{cn}: {a}\n".format(cn=c+1, a=poss[0]))
        if len(poss) > 1:
            print "Bad Magicisan"
            outfile.write("Case #{cn}: Bad magician!\n".format(cn=c+1))
