__author__="ozgur"
__date__ ="$May 21, 2011 7:08:52 PM$"


def solve(sq):
    num = len(sq)
    wp = []
    owp = []
    oowp = []
    for elem in sq:
        winCount = 0.0
        lossCount = 0.0
        for l in elem:
            if l == '1':
                winCount += 1.0
            elif l == '0':
                lossCount += 1.0

        wp.append(winCount / (winCount + lossCount))

    for i in range(num):
        sum = 0.0
        count = 0.0
        for elem in sq:
            winCount = 0.0
            lossCount = 0.0
            if not elem[i] == '.':
                count += 1.0
                for s in range(len(elem)):
                    if not s == i:
                        if elem[s] == '1':
                            winCount += 1.0
                        elif elem[s] == '0':
                            lossCount += 1.0
                sum += (winCount / (winCount + lossCount))
        if(count == 0.0):
            count = 1.0
        owp.append(sum / count)

    for i in range(num):
        elem = sq[i]
        lookat = []
        for s in range(len(elem)):
            if not (elem[s] == '.'):
                lookat.append(s)
        count = 0.0
        count += len(lookat)
        sum = 0.0
        for i in lookat:
            sum += owp[i]

        oowp.append(sum / count)

    rpi = []
    for i in range(num):
        rpi.append((0.25*wp[i]) + (0.50*owp[i]) + (0.25*oowp[i]))

    return rpi
    

def handle():
    square = []
    solutions = []
    T = int(raw_input())
    for i in range(T):
        N = int(raw_input())
        for i in range(N):
            line = raw_input()
            square.append(line)
        solutions.append(solve(square))
        square = []

    for i in range(T):
        print 'Case #' + str(i+1) + ':'
        for j in solutions[i]:
            print ("%0.12lf" %(j))


if __name__ == "__main__":
    handle()
