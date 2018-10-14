import numpy as np

def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        answer = 0
        r, t = map(int, fin.readline().strip().split(' '))

        s = 0
        i = r + 1
        while s <= t:
            s += i*i - (i-1)*(i-1)
            answer += 1
            i += 2

        answer -= 1
        print answer
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    # solve("A-tiny")
    solve("A-small-attempt0")
    # solve("A-large")