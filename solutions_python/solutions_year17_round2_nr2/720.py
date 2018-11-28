from collections import deque
import time
import math

def main():
    path = "C:\\Users\\user\\Dropbox\\Documents\\GoogleCodeJam2017\\B.Pony\\"
    with open(path + "result" + str(time.time()) + ".txt", 'w') as resF:
        T, vecs = readFile(path + "example.txt")#####
        print T
        print vecs
        for i in xrange(T):
            #t = time.time()
            sol = solve(vecs[i])
            line = "Case #" + str(i+1) + ": " + sol + "\n"
            print line
            resF.write(line)


def solve(vec):
    ColorToLetter = 'ROYGBV'
    N = vec[0]
    colors = vec[1:]

    last_chosen = -1
    s = ''
    for i in xrange(N):
        chosen = findNextPony(colors, last_chosen)
        if chosen == -1:
            return 'IMPOSSIBLE'
        last_chosen = chosen
        s += ColorToLetter[chosen]
        colors[chosen] -= 1

        #print s

    if s[0] == s[-1]:
        if len(s) < 4 or s[-2] == s[0] or s[-3] == s[-1]:
            return 'IMPOSSIBLE'
        else:
            s2 = list(s)
            temp = str(s2[-1])
            s2[-1] = str(s2[-2])
            s2[-2] = temp
            s = "".join(s2)
    return s


def findNextPony(colors, last_chosen):
    indxs = [0, 1, 2, 3, 4, 5]
    currentColors = list(colors)
    if not last_chosen == -1:
        for i in [last_chosen - 1, last_chosen, last_chosen + 1]:
            if i >= 6:
                i -= 6
            elif i < 0:
                i += 6
            currentColors[i] = -1000
    ind = currentColors.index(max(currentColors))
    # ind = [i for i, j in enumerate(currentColors) if j == max(currentColors)]
    if currentColors[ind] > 0:
        return ind
    else:
        return -1


def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        if len(lines) == 0:
            print "Err reading"
            return

        T = int(lines[0].replace("\n", ""))

        vecs = []
        for i in xrange(1, T+1):
            vecs.append(map(int, lines[i].split(" ")))

        return (T, vecs)

if __name__ == '__main__':
    main()


