__author__="ozgur"
__date__ ="$May 7, 2011 9:36:36 PM$"


T = 0
N = 0

def solve(seq):
    orange = []
    blue = []
    for s in seq:
        if s[0] == 'O':
            orange.append(s[1])
        else:
            blue.append(s[1])

    orangeLoc = 1
    blueLoc = 1
    time = 0
    done = False
    pressFlag = False

    while not done:
        if len(orange) == 0 and len(blue) == 0:
            done = True
        else:
            if len(orange) > 0:
                if orange[0] == orangeLoc:
                    if seq[0][0] == 'O':
                        seq.pop(0)
                        orange.pop(0)
                        pressFlag = True
                    else:
                        pass
                elif orange[0] > orangeLoc:
                    orangeLoc += 1
                elif orange[0] < orangeLoc:
                    orangeLoc -= 1

            if len(blue) > 0:
                if blue[0] == blueLoc:
                    if seq[0][0] == 'B':
                        if not pressFlag:
                            seq.pop(0)
                            blue.pop(0)
                    else:
                        pass
                elif blue[0] > blueLoc:
                    blueLoc += 1
                elif blue[0] < blueLoc:
                    blueLoc -= 1
                    
            pressFlag = False
            time += 1

    return time


def handle():
    global T,N
    sequence = []
    solutions = []
    T = int(raw_input())
    for i in range(T):
        line = raw_input()
        elements = line.split(' ')
        N = int(elements[0])
        for j in range(1, N + 1):
            sequence.append([elements[2*j -1], int(elements[2 * j])])
        solutions.append(solve(sequence))
        sequence = []

    for i in range(T):
        print 'Case #' + str(i+1) + ': ' + str(solutions[i])


if __name__ == "__main__":
    handle()
