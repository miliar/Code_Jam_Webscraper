import sys


def main():
    fileName = sys.argv[1]
    with open(fileName, 'r') as fin:
        line = fin.readline()
        T = int(line)
        for i in range(T):
            # process test cases
            answer1 = int(fin.readline()) - 1  # read first choise of a line
            a = []
            for j in range(4):
                a.append(map(int, fin.readline().split(' ')))
            answer2 = int(fin.readline()) - 1  # read second choise of a line
            b = []
            for j in range(4):
                b.append(map(int, fin.readline().split(' ')))
            setA = set(a[answer1])
            setB = set(b[answer2])
            setRes = setA.intersection(setB)
            if len(setRes) > 1:
                resultString = 'Bad magician!'
            if len(setRes) == 0:
                resultString = 'Volunteer cheated!'
            if len(setRes) == 1:
                resultString = str(setRes.pop())
            with open(fileName + '.out', 'a') as fout:
                print >> fout, 'Case #' + str(i + 1) + ': ' + resultString

if __name__ == '__main__':
    main()
