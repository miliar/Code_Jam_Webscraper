'''
Created on 3/18/17

@author: junkang

'''


def loadInput(filename):
    input = []
    with open(filename, 'r') as f:
        for l in f:
            line = l.strip()
            if len(line) == 0:
                continue
            input.append(line)
    return input[1:]



def find_flips(inp):
    # print inp.split()
    pancakes = list(inp.split()[0])
    # if len(pancakes) < 3:
    #     return -1
    try:
        k = int(inp.split()[1])
    except:
        # print "Cannot get k", inp
        k = 3

    flips = -1 if pancakes.count('-') > 0 else 0

    def get_key(pc, i):
        return str(pc)+"#"+str(i)


    def _flips(pc, i, count, hist, k):
        # print pc, i, count
        key = get_key(pc, i)
        if key in hist:
            return count + hist[key]

        if i > len(pc) - k:
            return count if pc.count('-') == 0 else -1

        # print ''.join(pc[i:i+k]), '+'*k
        # if ''.join(pc[i:i+k]) != '+'*k:
        pc_flip = pc[:]

        for j in range(i, i+k):
            pc_flip[j] = '-' if pc_flip[j] == '+' else '+'

        cnt_noflip = _flips(pc, i + 1, count, hist, k)
        cnt_flip = _flips(pc_flip, i+1, count+1, hist, k)

        key_noflip = get_key(pc, i+1)
        key_flip = get_key(pc_flip, i+1)

        hist[key_noflip] = cnt_noflip - count
        hist[key_flip] = cnt_flip - count - 1

        cnt = min(cnt_flip, cnt_noflip)
        cnt_max = max(cnt_flip, cnt_noflip)
        if cnt == -1 and cnt != cnt_max:
            return cnt_max
        return cnt



    hist = {}
    for i in range(len(pancakes)-k+1):
        flips = _flips(pancakes[:], i, 0, hist, k)
        # break
        if flips > -1:
            break

    return str(flips) if flips > -1 else 'IMPOSSIBLE'



def saveOutput(outputs, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(outputs))
    print '- output:', filename

if __name__ == '__main__':
    filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_A/A-small-attempt1.in', '/Users/junkang/Projects/codejam/qual_A/A-small-attempt1.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_A/A-small-attempt0.in', '/Users/junkang/Projects/codejam/qual_A/A-small-attempt0.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_A/test', '/Users/junkang/Projects/codejam/qual_A/test.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_A/test', '/Users/junkang/Projects/codejam/qual_A/test.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/2016/qual_B/B-small-practice.in', '2016_qual_B-small-practice.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/2016/qual_B/B-large-practice.in', '2016_qual_B-large-practice.out'
    # filename_in, filename_out = '2017_qual_A-small-practice.in', '2017_qual_A-small-practice.out'
    # filename_in, filename_out = '2017_qual_A-large-practice.in', '2017_qual_A-large-practice.out'

    input = loadInput(filename_in)

    outputs = []
    for i, inp in enumerate(input):
        ret = find_flips(inp)
        output = 'Case #%d: %s'%(i+1, ret)
        print '%15s => %s'%(inp, output)
        outputs.append(output)

    saveOutput(outputs, filename_out)
