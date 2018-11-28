#!/usr/bin/env python

def main():
    fin = open('A-large.in', 'r')
    fout = open('out.out', 'w')
    N = int(fin.readline().strip('\n'))
    for casenum in range(1, N+1):
        keys = fin.readline().strip('\n').split()
        numkeys = int(keys[0])
        keys = keys[1:]
        bluePos = 1
        orangePos = 1
        numMoves = 0
        cont = True
        while True:
            remove = False
            if len(keys) == 0:
                break
            numMoves += 1
            if 'B' in keys:
                blue = keys.index('B')
            else:
                blue = -1
            if 'O' in keys:
                orange = keys.index('O')
            else:
                orange = -1
            if blue >= 0:
                NBpos = int(keys[blue+1])
                if blue == 0 and bluePos == int(keys[1]):
                    remove = True
                elif NBpos > bluePos:
                    bluePos += 1
                elif NBpos < bluePos:
                    bluePos -= 1
                    
            if orange >= 0:
                NOpos = int(keys[orange+1])
                if orange == 0 and orangePos == int(keys[1]):
                    remove = True
                elif NOpos > orangePos:
                    orangePos += 1
                elif NOpos < orangePos:
                    orangePos -= 1
            if remove:
                keys.pop(0)
                keys.pop(0)
        print numMoves
        
            
        fout.write('Case #%d: %d\n' % (casenum, numMoves))
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()