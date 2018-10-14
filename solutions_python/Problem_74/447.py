from sys import stdin

T = int(stdin.readline())
for t in xrange(0, T):
    line = stdin.readline().split(' ')
    N = int(line[0])
    seq = []
    Oseq = []
    Bseq = []
    for n in xrange(0, N):
        nextChar = line[1 + (2 * n)]
        nextInt = int(line[1 + (2 * n) + 1])
        seq.append(nextChar)
        if nextChar == 'O':
            Oseq.append(nextInt)
        else:
            Bseq.append(nextInt)
    time = 0
    Opos = 1
    Bpos = 1
    Oturn = 0
    Bturn = 0
    for turn in seq:
        if (turn == 'O'):
            Onext = Oseq[Oturn]
            if (Opos < Onext):
                last = Onext - Opos + 1
            elif (Opos > Onext):
                last = Opos - Onext + 1
            else:
                last = 1
            time = time + last
            Opos = Onext
            Oturn = Oturn + 1

            if (Bturn < len(Bseq)):
                Bnext = Bseq[Bturn]
                if (Bpos < Bnext):
                    if (Bpos + last) < Bnext:
                        Bpos = Bpos + last
                    else:
                        Bpos = Bnext
                elif (Bpos > Bnext):
                    if (Bpos - last) > Bnext:
                        Bpos = Bpos - last
                    else:
                        Bpos = Bnext
        else:
            Bnext = Bseq[Bturn]
            if (Bpos < Bnext):
                last = Bnext - Bpos + 1
            elif (Bpos > Bnext):
                last = Bpos - Bnext + 1
            else:
                last = 1
            time = time + last
            Bpos = Bnext
            Bturn = Bturn + 1
            
            if (Oturn < len(Oseq)):
                Onext = Oseq[Oturn]
                if (Opos < Onext):
                    if (Opos + last) < Onext:
                        Opos = Opos + last
                    else:
                        Opos = Onext
                elif (Opos > Onext):
                    if (Opos - last) > Onext:
                        Opos = Opos - last
                    else:
                        Opos = Onext
    print 'Case #' + str(t + 1) + ': ' + str(time)

