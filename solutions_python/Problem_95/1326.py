plain = ' abcdefghijklmnopqrstuvwxyz\n'
trans = ' ynficwlbkuomxsevzpdrjgthaq\n'


infile = open("A-small-attempt0.in","r")
outfile = open("A-small.out","w")

T = int(infile.readline())
for test in xrange(1,T+1):
    case = infile.readline()
    answer = ''
    for i in case:
        answer += plain[trans.index(i)]
    outfile.write("Case #" + str(test) + ": " + answer)

infile.close()
outfile.close()
