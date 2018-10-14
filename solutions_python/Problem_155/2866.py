

if __name__ == '__main__':

    import sys

    # reads input file name
    f = sys.argv[1]


    infile = open(f+'.in', 'r')
    outfile = open(f+'.out', 'w')

    state = 0
    caseNo = 0

    for line in infile:

        if state == 0:

            n = int(line)
            state += 1

        elif state == 1:

            caseNo += 1
            str = line.split()[1]
            clap = 0
            friends = 0

            for x in str:
                clap += int(x)
                if clap < 1:
                    # insufficient clap, add 1 friend
                    friends += 1
                else:
                    # remove 1 clap
                    clap -= 1

            # print '%s' % clap
            outfile.write('Case #%s: %s\n' % (caseNo, friends))