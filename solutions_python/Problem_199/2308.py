with open('input.txt', 'rU') as f:
    with open('output.txt', 'w') as fout:
        lines = f.readlines()

        for i, n in enumerate(lines):
            line = n.rstrip()
            if i > 0 and line != '':
                fout.write('Case #')
                fout.write(str(i))
                fout.write(': ')

                seq = list(line.split()[0])
                length = int(line.split()[1])

                flag = True
                count = 0
                for i, ch in enumerate(seq):
                    if i <= len(seq) - length:
                        if ch == '-':
                            count += 1
                            for j in xrange(i, i + length):
                                seq[j] = '+' if seq[j] == '-' else '-'
                    else:
                        if ch == '-':
                            flag = False
                            break
                if flag:
                    fout.write(str(count) + '\n')
                else:
                    fout.write('IMPOSSIBLE\n')
