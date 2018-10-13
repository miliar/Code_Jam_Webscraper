import itertools
from multiprocessing import Pool

def isUpAndDown(seq):
    down = False
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            down = True
        else:
            if down:
                return False
    return True

def inversionNumber(seq1, seq2):
    number = 0
    for i in range(len(seq1)):
        index = seq2.index(seq1[i])
        number += index
        seq2.pop(index)
    return number


def testCase(A):
    min = -1
    for permutation in itertools.permutations(A, len(A)):
        if isUpAndDown(permutation):
            number = inversionNumber(A, list(permutation))
            if number < min or min == -1:
                min = number
    print(min)
    return min

if __name__ == '__main__':
    with open('B.in') as f:
        with open('B.out', 'w') as f2:
            lines = f.readlines()
            output = ""

            As = []

            for i in range(int(lines[0])):
                N = int(lines[i*2+1])
                A = [int(x) for x in lines[i*2+2].split(" ")]

                As.append(A)

            p = Pool(10)
            cases = p.map(testCase, As)
            p.close()
            p.join()

            for i in range(len(cases)):
                output += "Case #" + str(i+1) + ": " + str(cases[i]) + "\n"

            print(output)
            f2.write(output)