__author__ = 'isaac'

def main(filein):
    fid = open(filein, 'r')
    T = int(fid.readline().rstrip('\n'))
    print 'Number of cases: ', str(T)
    R = []
    for zzz in range(0,T):
        solution = 0
        row1 = int(fid.readline().rstrip('\n'))
        m1 = [fid.readline().rstrip('\n').split()]
        m1 += [fid.readline().rstrip('\n').split()]
        m1 += [fid.readline().rstrip('\n').split()]
        m1 += [fid.readline().rstrip('\n').split()]
        row2 = int(fid.readline().rstrip('\n'))
        m2 = [fid.readline().rstrip('\n').split()]
        m2 += [fid.readline().rstrip('\n').split()]
        m2 += [fid.readline().rstrip('\n').split()]
        m2 += [fid.readline().rstrip('\n').split()]

        set1 = set(m1[row1-1])
        set2 =  set(m2[row2-1])
        intersection_len = len(set1.intersection(set2))
        if intersection_len == 0:
            solution = 'Volunteer cheated!'
        elif intersection_len == 1:
            solution = str(list(set1.intersection(set2))[0])
        else:
            solution = 'Bad magician!'
        R.append(solution)

    fileout = filein[0:-2] + 'out'
    fid = open(fileout,'w')
    idx = 1
    for line in R:
        h = 'Case #' + str(idx) + ': '
        hh = h + ''.join(str(line)) + '\n'
        fid.write(hh)
        idx += 1
    fid.close()

#main('sample.in')
main('A-small-attempt0.in')