with open('input.txt', 'rU') as f:
    with open('output.txt', 'w') as fout:
        lines = f.readlines()
        count = str(lines[0])

        for i, n in enumerate(lines):
            number = n.rstrip()
            if i > 0 and number != '':
                fout.write('Case #')
                fout.write(str(i))
                fout.write(': ')

                rst = number

                while True:
                    pos = 0
                    m = rst[0]
                    for j, digit in enumerate(rst):
                        if digit < m:
                            pos = j
                            break
                        if digit > m:
                            m = digit
                    if pos == 0:
                        break
                    else:
                        s = rst[0:pos]
                        d = int(s) - 1
                        t = ''
                        if d > 0: t = str(d)
                        t += '9' * (len(rst) - pos)
                        rst = t
                fout.write(rst + '\n')
