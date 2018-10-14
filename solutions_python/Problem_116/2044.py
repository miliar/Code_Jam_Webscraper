#!/usr/bin/python

XWin = ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']
OWin = ['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO']

iter = int(raw_input())

for i in range(iter):
    # Storage input tic, last two entry for diagonal
    inputs = ['', '', '', '', '', '', '', '', '', '']
    determined = False
    notcompleted = False

    for j in range(4):
        inputs[j] = raw_input()

    # Get empty line between cases
    if i < iter - 1:
        raw_input()

    # Get diagonal and columns
    for j in range(4):
        thisline = inputs[j]
        inputs[4] += thisline[j]
        inputs[5] += thisline[3 - j]
        inputs[6] += thisline[0]
        inputs[7] += thisline[1]
        inputs[8] += thisline[2]
        inputs[9] += thisline[3]

    # Tell if anyone win
    for j in range(10):
        # print inputs[j]
        if inputs[j] in XWin:
            print "Case #%d: X won" %(i + 1)
            determined = True
            break
        elif inputs[j] in OWin:
            print "Case #%d: O won" %(i + 1)
            determined = True
            break

    if determined:
        continue

    for j in range(4):
        if '.' in inputs[j]:
            notcompleted = True
            print "Case #%d: Game has not completed" %(i + 1)
            break

    if notcompleted:
        continue
    else:
        print "Case #%d: Draw" %(i + 1)
