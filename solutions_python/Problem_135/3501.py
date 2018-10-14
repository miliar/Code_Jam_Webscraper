import argparse
import re

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', nargs = 1, metavar = 'INPUT', help = "Input file", required = True, dest = 'input_file')
    return parser.parse_args()    


if __name__ == "__main__" :

    args = args()

    if args.input_file[0] is not None:
        input_file = args.input_file[0]
    else:
        logger.error('Error: no input_file.')
        sys.exit(-1)

    output = ''

    with open(input_file, 'r') as f:
        lines = f.readlines()
        numTest = int(lines[0].strip())
        i = 0
        while i < numTest:
            start = 10*i + 1
            res1 = int(lines[start].strip())
            line1 = lines[start + res1]
            set1 = map(int, re.findall(r'^(\d+)\s(\d+)\s(\d+)\s(\d+)',line1)[0])
            start += 5
            res2 = int(lines[start].strip())
            line2 = lines[start + res2]
            set2 = map(int, re.findall(r'^(\d+)\s(\d+)\s(\d+)\s(\d+)',line2)[0])
            test_res = set(set1).intersection(set(set2))
            output += 'Case #' + str(i+1) + ': '
            if len(test_res) == 1:
                output += str(test_res.pop())
            elif len(test_res) > 1:
                output += 'Bad magician!'
            else:
                output += 'Volunteer cheated!'
            if numTest != i+1:
                output += '\n'
            i += 1

    print output

    with open('output1.txt', 'w') as f:
        f.write(output)
    