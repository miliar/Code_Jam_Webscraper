f_in = open('input.txt')
f_out = open('output.txt', 'w')
t = int(f_in.readline())

for testcase in range(t):
    n = int(f_in.readline())
    meds = []
    for i in range(n):
        st = f_in.readline().strip()

        # split
        seq = []
        last_seq = st[0]
        current = ''
        for j in range(len(st)):
            if st[j] == last_seq:
                current += st[j]
            else:
                seq.append(current)
                last_seq = st[j]
                current = st[j]
        seq.append(current)

        med = []
        for k in range(len(seq)):
            med.append((seq[k][0], len(seq[k])))

        meds.append(med)

    answer = ''

    med_len = len(meds[0])
    for l in range(n):
        if len(meds[l]) != med_len:
            answer = 'Fegla Won'
            break
        # TODO ar atitinka raides

    if not answer:
        for r in range(med_len):
            target = meds[0][r][0]
            for s in range(n):
                if meds[s][r][0] != target:
                    print meds[s][r][0], target
                    answer = 'Fegla Won'
                    break
            if answer:
                break

    if not answer:
        avgs = []
        answer = 0
        for m in range(med_len):
            summed = 0
            for o in range(n):
                summed += meds[o][m][1]
            avgs.append(summed / n)

        for p in range(med_len):
            chn = 0
            for q in range(n):
                chn += abs(avgs[p] - meds[q][p][1])
            answer += chn
            print "...", chn

    print answer
    print "==="

    f_out.write('Case #{0}: {1}\n'.format(testcase + 1, answer))

f_out.close()
