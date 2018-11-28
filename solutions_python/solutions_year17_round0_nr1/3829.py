#!/usr/bin/python

uses_flip = 0

def testflip(tb, bw, abw):
    global uses_flip, panc

    if abw < 0 or bw >= (sizepanc-flip+1) or uses_flip > (sizepanc-flip+1):
        return (sizepanc-flip+2)

    subpanc = panc[abw:abw+flip]

    if subpanc[-1] != '0':
        return min(testflip(tb, bw+1, abw-1),
                    testflip(tb, bw+2, abw-2))

    subpanc = int(subpanc,2)
    newpanc = bin(subpanc ^ tb)
    newpanc = newpanc.replace('0b','')

    if len(newpanc) < flip:
        newpanc = str('0' * (flip-len(newpanc)) )+newpanc

    panc = panc[:abw] + newpanc + panc[abw+flip:]
    uses_flip += 1

    check = int(panc,2)
    if '0' not in panc:
        return uses_flip

    # minimo de uses_flip para pb all 1
    return min(testflip(tb, bw+1, abw-1),
                testflip(tb, bw+2, abw-2))

t = int(input())
for i in range(1, t+1):
    uses_flip = 0
    line = input().split(' ')
    panc, flip = (line[0], int(line[1]))
    sizepanc = len(panc)
    panc = panc.replace('-','0').replace('+','1')
    # print('0' not in panc, panc)
    if '0' not in panc:
        print('Case #%s: 0' % i)
    else:
        result = testflip(int('1'*flip,2), 0, sizepanc-flip)
        if(result > (sizepanc-flip+1)):
            print('Case #%s: IMPOSSIBLE' % i)
        else:
            print('Case #%s: %d' % (i, result))
