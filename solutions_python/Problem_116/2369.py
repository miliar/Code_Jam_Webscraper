import itertools


def main():
    filename = 'A-large.in'
    input = open(filename, 'r')

    tests_count = int(input.readline().strip())

    output = open('A-large.out', 'w')

    for case in xrange(tests_count):
        field = []
        for j in xrange(4):
            field.append(input.readline().strip())

        summ_h_list = []
        summ_v_list = []
        summ_d1 = 0
        summ_d2 = 0
        summ_h_list_o = []
        summ_v_list_o = []
        summ_d1_o = 0
        summ_d2_o = 0
        point_present = False
        for i in xrange(4):
            summ_h = 0
            summ_v = 0
            summ_h_o = 0
            summ_v_o = 0

            if field[i][i] in ['X', 'T']:
                summ_d1 += 1
            if field[i][i] in ['O', 'T']:
                summ_d1_o += 1
            if field[i][3 - i]  in ['X', 'T']:
                summ_d2 += 1
            if field[i][3 - i]  in ['O', 'T']:
                summ_d2_o += 1
            for j in xrange(4):
                if field[i][j] == '.':
                    point_present = True
                if field[i][j] in ['X', 'T']:
                    summ_h += 1
                if field[i][j] in ['O', 'T']:
                    summ_h_o += 1
                if field[j][i] in ['X', 'T']:
                    summ_v += 1
                if field[j][i] in ['O', 'T']:
                    summ_v_o += 1
            summ_h_list.append(summ_h)
            summ_v_list.append(summ_v)

            summ_h_list_o.append(summ_h_o)
            summ_v_list_o.append(summ_v_o)

        l = [summ_d1, summ_d2]
        l.extend(summ_h_list)
        l.extend(summ_v_list)
        l_o = [summ_d1_o, summ_d2_o]
        l_o.extend(summ_h_list_o)
        l_o.extend(summ_v_list_o)
        if 4 in l:
            #print 'Case #{0}: X won'.format(case + 1)
            output.write('Case #{0}: X won\n'.format(case + 1))
        elif 4 in l_o:
            #print 'Case #{0}: O won'.format(case + 1)
            output.write('Case #{0}: O won\n'.format(case + 1))
        elif point_present:
            #print 'Case #{0}: Game has not completed'.format(case + 1)
            output.write('Case #{0}: Game has not completed\n'.format(case + 1))
        else:
            #print 'Case #{0}: Draw'.format(case + 1)
            output.write('Case #{0}: Draw\n'.format(case + 1))

        input.readline()

if __name__ == '__main__':
    main()
