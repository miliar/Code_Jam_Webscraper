reader = open('A-small-attempt0.in')
writer = open('output-small', 'w')

test_cases = int(reader.readline())

for i in range(test_cases):
    line = reader.readline()[:-1].split(' ')
    N = int(line[0])
    Pd = int(line[1])
    Pg = int(line[2])

    p = False

    for n_i in range(1, N+1):
        if n_i * Pd / 100.0 == n_i * Pd / 100:
            # possible that you've played n_i games today
            wins_today = Pd * n_i
            if Pg == 0 and wins_today > 0:
                p = False
            elif Pg == 100 and Pd <> 100:
                p = False
            else:
                p = True
                break

    if p:
        writer.write('Case #%s: Possible' % (i + 1) + '\n')
    else:
        writer.write('Case #%s: Broken' % (i + 1) + '\n')
        

reader.close()
writer.close()
