#!/usr/bin/env python


def makeseq(inp):
    processed = inp.split()[1:]
    seq = []
    for i in range(len(processed) / 2):
        seq.append((processed[2*i], int(processed[2*i+1])))
    return seq

def nextmove(seq, color):
    for move in seq:
        if move[0] == color:
            return move
    return None

def move(pos, dest):
    if pos < dest:
        return pos + 1
    else:
        return pos - 1


def counttime(seq):
    count = 0
    bluepos = 1
    orangepos = 1
    bluemove = nextmove(seq, 'B')
    orangemove = nextmove(seq, 'O')
    pushingbutton = False
    while seq != []:
        bluemove = nextmove(seq, 'B')
        orangemove = nextmove(seq, 'O')
        if bluemove != None:
            if bluemove[1] == bluepos:
                if seq[0][0] == 'B':
                    seq.remove(bluemove)
                    bluemove = nextmove(seq, 'B')
                    pushingbutton = True
            else:
                bluepos = move(bluepos, bluemove[1])
        if orangemove != None:
            if orangemove[1] == orangepos:
                if seq[0][0] == 'O' and not pushingbutton:
                    seq.remove(orangemove)
                    orangemove = nextmove(seq, 'O')
            else:
                orangepos = move(orangepos, orangemove[1])
        count += 1
        pushingbutton = False
    return count


def main():
    cases = input()
    results = []
    for i in range(cases):
        inp = raw_input()
        seq = makeseq(inp)
        results.append(counttime(seq))
    for result in range(len(results)):
        print 'Case #' + str((result + 1)) + ': ' + str(results[result])


if __name__ == '__main__':
    main()
