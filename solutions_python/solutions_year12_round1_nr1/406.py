import sys

def calc_keystrokes(word, total):
    ks = []
    for i in range(len(word) + 1):
        k = 2 * i + (total - len(word)) + 1
        if 'X' in word[:len(word) - i]:
            k = k + total + 1
        ks.append(k)
    ks.append(1 + total + 1)
    return ks

def compute(*args):
    entered = args[0]
    total = args[1]
    pos = args[2:]
    pos_map = {}
    words = ['',]
    for i in range(entered):
        new_words = []
        for w in words:
            new_words.append(w + '.')
            new_words.append(w + 'X')
        words = new_words
    for word in words:
        word_pos = 1
        for lnum, l in enumerate(word):
            if l == '.':
                word_pos *= pos[lnum]
            else:
                word_pos *= 1 - pos[lnum]
        pos_map[word] = word_pos
    res = []
    for word in pos_map:
        ks = calc_keystrokes(word, total)
        for i, k in enumerate(ks):
            kp = k * pos_map[word]
            if len(res) <= i:
                res.append(kp)
            else:
                res[i] = res[i] + kp
    return '%.6f' % min(*res)

def execute(intxt):
    lines = intxt.split('\n')
    tests_total = int(lines[0])
    outtxt = ''
    for test_num, line_num in enumerate(range(1, tests_total * 2 + 1, 2)):
        outtxt += "Case #%s: %s\n" % (test_num + 1, compute(*(map(int, lines[line_num].split(' ')) +
                                                          map(float, lines[line_num + 1].split(' ')))))
    return outtxt[:-1]

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    with open(infile, 'r') as _ifile:
        with open(outfile, 'wb') as _ofile:
            _ofile.write(execute(_ifile.read()))