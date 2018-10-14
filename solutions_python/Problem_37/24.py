# Instructions: run main().

import sys

def main():
    problemLetter = 'A'
    #filePrefix = '%s-sample' % problemLetter
    filePrefix = '%s-small-attempt0' % problemLetter
    #filePrefix = '%s-large' % problemLetter
    fin = open(filePrefix + '.in', 'r')
    fout = open(filePrefix + '.out', 'w')
    #fout = sys.stdout
    caseCount = int(fin.readline().strip())

    for caseIx in range(caseCount):
        bases = [int(s) for s in fin.readline().strip().split()]
        #print bases
        i = 2
        while True:
            maybe = True
            for b in bases:
                if not happy(b, i, set([])):
                    maybe = False
                    break
            if maybe == True: break
            i += 1


        fout.write('Case #%d: %d\n' % (caseIx + 1, i))

    fin.close()
    if fout != sys.stdout: fout.close()


def happy(b, i, bads):
    if i in bads:
        return False
    rem, h, bb = i, 0, b
    while rem > 0:
        h += (rem % bb)**2
        rem /= b
    if h == 1:
        return True
    else:
        bads.add(i)
        return happy(b, h, bads)

    
