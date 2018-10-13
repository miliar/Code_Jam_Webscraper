def solve(filename):
    with open(filename, 'r') as fin:
        lines = fin.readlines()
        ncase = int(lines[0][:-1])
        for i in range(1, ncase+1, 1):
            member = 0
            current = 0
            smax, bits = lines[i][:-1].split(' ')
            smax = int(smax)
            bits = [int(b) for b in bits]
            for k in range(smax+1):
                if bits[k] != 0:
                    if current >= k:
                        current += bits[k]
                    else:
                        member += k - current
                        current += bits[k] + (k - current)

            with open('result.out', 'a') as fout:
                fout.writelines('Case #' + str(i) + ": " + str(member) + '\n')



solve('A-large.in')