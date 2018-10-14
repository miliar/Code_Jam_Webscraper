casenum = 1
def doit(case):
    global casenum
    case = list(reversed((case.split(' '))[1:]))

    seqs = {'O': [], 'B': []}
    
    seqnum = 0
    while len(case) != 0:
        key, val = case.pop(), int(case.pop())
        seqs[key].append({
            'pos' : val,
            'seq' : seqnum
        })
        seqnum += 1

    robpos = {
        'O' : 1,
        'B' : 1
    }
    steps = 0
    
    seqnum = 0
    while len(seqs['O']) > 0 or len(seqs['B']) > 0:
        gonext = False
        for robot in 'OB':
            if len(seqs[robot]) == 0:
                continue

            target = seqs[robot][0]
            curpos = robpos[robot]
            if target['pos'] != curpos:
                d = target['pos'] - curpos
                robpos[robot] += d/abs(d)
            elif target['seq'] == seqnum:
                gonext = True
                del seqs[robot][0]

        steps += 1

        if gonext:
            seqnum += 1

    print 'Case #%d: %d' % (casenum, steps)
    casenum += 1

raw = [x.strip() for x in open('A-large.in').readlines()]
ZZZ = int(raw[0])
data = raw[1:]
for case in range(ZZZ):
    doit(data[case])
