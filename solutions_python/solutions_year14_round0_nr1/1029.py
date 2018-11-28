import sys
import numpy as np

def parse(filename):
    cases = []
    with open(filename) as fp:
        line = fp.readline().strip()
        nr_cases = int(line)
        for i in range(nr_cases):
            case = []
            case.append(int(fp.readline()))
            arr = np.zeros((4,4))
            for j in range(4):
                arr[j,:] = np.array(map(int, fp.readline().split(' ')))
            case.append(arr)
            case.append(int(fp.readline()))
            arr = np.zeros((4,4))
            for j in range(4):
                arr[j,:] = np.array(map(int, fp.readline().split(' ')))
            case.append(arr)
            cases.append(case)
    return cases

def evaluate(cases):
    output = ''
    for i, case in enumerate(cases):
        if case[0] > 4:
            output += "Case #%d: Volunteer cheated!\n" % (i + 1)
            continue
        row = case[1][case[0] - 1]
        print row
        # find columns
        row_idxs = [None for _ in range(4)]
        for j in range(4):
            for k in range(4):
                if row[j] in case[3][k]:
                    row_idxs[j] = k
                    break
        print i, row_idxs, case[2] - 1
        possible_idxs = row_idxs.count(case[2] - 1)
        if possible_idxs == 1:
            card = row[row_idxs.index(case[2] - 1)]
            output += "Case #%d: %d\n" % (i +1, card)
        else:
            if case[2] - 1 not in row_idxs:
                output += "Case #%d: Volunteer cheated!\n" % (i + 1)
            else:
                output += "Case #%d: Bad magician!\n" % (i + 1)
        # elif possible_idxs == 0:
        #     output += "Case #%d: Volunteer cheated!\n" % (i + 1)
        # else:
    print output
    assert len(output.strip().split('\n')) == len(cases)
    return output

if __name__ == '__main__':
    fn = sys.argv[1]
    out = fn + ".out"

    cases = parse(fn)

    output = evaluate(cases)

    with open(out, 'w') as fp:
        fp.write(output)