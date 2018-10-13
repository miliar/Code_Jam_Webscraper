input_file = 'B-large.in'
# input_file = 'b.in'
output_file = 'B.out'

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = int(f.readline())
        for case_nr in xrange(1, cases+1):
            line = f.readline()[:-1]
            print line
            ans = line
            if len(line) > 1:
                # go deeper as long seq is nondecreasing
                # if decreasing go back one decrease and set all 9
                i = 0
                decreasing = False
                while i < len(line)-1:
                    if line[i] > line[i + 1]:
                        decreasing = True
                        break
                    i += 1
                # print 'decreasing', decreasing
                if decreasing:
                    if i > 0:
                        i -= 1
                        while line[i] == line[i+1] and i >= 0:
                            i -= 1
                        # print 'i', i
                        if i == -1:
                            if line[0] != '1':
                                ans = chr(ord(line[0])-1) + ('9' * (len(line) - 1))
                            else:
                                ans = '9' * (len(line) - 1)
                        else:
                            i += 1
                            line = list(line)
                            line[i] = chr(ord(line[i])-1)
                            for k in range(i+1, len(line)):
                                line[k] = '9'
                            ans = ''.join(line)
                    else:
                        if line[0] != '1':
                            ans = chr(ord(line[0]) - 1) + ('9' * (len(line) - 1))
                        else:
                            ans = '9' * (len(line) - 1)

            print 'Case #{i}: {res}'.format(res=ans, i=case_nr)
            out.write('Case #{i}: {res}\n'.format(res=ans, i=case_nr))
