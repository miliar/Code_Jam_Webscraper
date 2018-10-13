import numpy as np
import sys

def main(input, output):
    f = open(output, 'w')
    T = None
    loop = 1
    for line in file(input):
        if T is None:
            T = int(line.strip())
            continue
        A, B = np.array(map(int, line.strip().split(' ')))
        lookup = np.zeros((B + 1), dtype = np.int8)
        #lookup = np.zeros((B + 1))
        num_recycled = 0
        for n in range(A, B + 1):
            if lookup[n] > 0:
                continue

            orig = '%s' % n
            transpose = np.array(list(orig))
            strlen = np.size(transpose)

            allpairs = []
            for j in range(1, strlen):
                element = transpose[-1]
                transpose = np.insert(np.delete(transpose, -1), 0, '%s' % element)
                m = int("".join(transpose))
                if m > n and m <= B and lookup[m] == 0:
                    #lookup[n] = 1
                    lookup[m] = 1
                    num_recycled += 1
                    allpairs.append(m)
            for i in range(0, len(allpairs)):
                for j in range(i + 1, len(allpairs)):
                    num_recycled += 1

        #f.write('Case #%s: %s (%s)\n' % (loop, num_recycled, np.sum(lookup)))
        f.write('Case #%s: %s\n' % (loop, num_recycled))
        loop += 1

if __name__ == '__main__':
    if len(sys.argv) != 3:
        quit('python recycle.py <input file> <output file>')
    main(sys.argv[1], sys.argv[2])