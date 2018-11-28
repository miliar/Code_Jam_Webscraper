import sys
import re

def main():
    infile = open(sys.argv[1])
    T = int(infile.readline().strip())

    pattern = re.compile('\s*([BO]) (\d+)')
    for i in range(0, T):
        B = []
        O = []
        seq = []
        line = infile.readline().strip()
        line = re.sub('^\d+ ', '', line)
        while(line):
            m = pattern.match(line)
            if m.group(1) == 'B':
                B.append(m.group(2))
                seq.append('B')
            else:
                O.append(m.group(2))
                seq.append('O')
            line = pattern.sub('', line, 1)
        B.reverse()
        O.reverse()
        time = 0
        bmoved = 0
        omoved = 0
        bpos = 1
        opos = 1
        for j in range(0, len(seq)):
            if seq[j] == 'B':
                move = int(B.pop())
                steps = abs(bpos - move) + 1
                if steps - omoved > 0:
                    steps = steps - omoved
                else:
                    steps = 1
                bmoved += steps
                omoved = 0
                time += steps
                bpos = move
            else:
                move = int(O.pop())
                steps = abs(opos - move) + 1
                if steps - bmoved > 0:
                    steps = steps - bmoved 
                else:
                    steps = 1
                omoved += steps
                bmoved = 0
                time += steps
                opos = move
        print "Case #" + str(i+1) + ": " + str(time)

if __name__ == "__main__":
    main()
