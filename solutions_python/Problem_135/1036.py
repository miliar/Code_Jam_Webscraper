if __name__ == "__main__":
    infile = 'D:\A-small-attempt0.in'
    outfile = 'D:\output.txt'
    outlns = []
    lns = [ln.strip() for ln in open(infile).readlines() if ln.strip() != '']

    cases = int(lns[0])
    for i in range(cases):
        ans1 = int(lns[i*10 + 1])
        rows1 = [set(row.split(' ')) for row in lns[i*10 + 2:i*10 + 6]]
        ans2 = int(lns[i*10+6])
        rows2 = [set(row.split(' ')) for row in lns[i*10+7:i*10+11]]

        mutualdata = rows1[ans1-1].intersection(rows2[ans2-1])
        if len(mutualdata) == 1:
            outlns.append('Case #' + str(i+1) + ': ' + str(mutualdata.pop()) + '\n')
        elif len(mutualdata) > 1:
            outlns.append('Case #' + str(i+1) + ': ' + 'Bad magician!\n')
        elif len(mutualdata) == 0:
            outlns.append('Case #' + str(i+1) + ': ' + 'Volunteer cheated!\n')
        else:
            print 'something wrong!'

    f = open(outfile, 'w')
    f.writelines(outlns)
    f.close()