'''
Created on 3/18/17

@author: junkang

'''
import sys
sys.setrecursionlimit(1500)

def loadInput(filename):
    input = []
    with open(filename, 'r') as f:
        for l in f:
            line = l.strip()
            if len(line) == 0:
                continue
            input.append(list(line))

    print len(input)
    return input[1:]


def get_tidy_num(num):
    # print num

    if len(num) == 1:
        return num

    # 1101 -> 999
    for i in range(len(num)-1, 0, -1):
        n=int(num[i])
        nn = int(num[i-1])
        if n < nn:
            num[i-1] = str(nn-1)
            num[i:] = '9'*(len(num)-i)

    return num if num[0] is not '0' else num[1:]


def saveOutput(outputs, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(outputs))
    print '- output:', filename

if __name__ == '__main__':
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_B/test.in', '/Users/junkang/Projects/codejam/qual_B/test.out'
    filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_B/B-large.in', '/Users/junkang/Projects/codejam/qual_B/B-large.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_B/B-small-attempt1.in', '/Users/junkang/Projects/codejam/qual_B/B-small-attempt1.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_B/B-small-attempt0.in', '/Users/junkang/Projects/codejam/qual_B/B-small-attempt0.out'


    input = loadInput(filename_in)
    # input = []

    outputs = []
    for i, inp in enumerate(input):

        ret = get_tidy_num(inp)
        output = 'Case #%d: %s'%(i+1, ''.join(ret))
        print '%15s => %s'%(''.join(inp), output)
        outputs.append(output)

    saveOutput(outputs, filename_out)
