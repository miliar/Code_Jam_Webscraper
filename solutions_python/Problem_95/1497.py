import sys
import string

def solver(s, trans_table):
    return string.translate(s, trans_table)

def ssi(s):
    """
    space separated integers
    """
    return map(int, s.strip('\n').split())

def rl():
    return sys.stdin.readline()

def debug(msg='', off=False):
    if not off:
        sys.stderr.write(str(msg) + '\n')

def main():
    # open input file
    # input_file = open('infile.txt')
    strings = [
            ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
                'our language is impossible to understand'],
            ['rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
                'there are twenty six factorial possibilities'],
            ['de kr kd eoya kw aej tysr re ujdr lkgc jv',
                'so it is okay if you want to just give up',]
            ]
    trans = {'y': 'a', 'e': 'o', 'q': 'z'}
    for from_s, to_s in strings:
        for c_idx in xrange(len(from_s)):
            from_c = from_s[c_idx]
            to_c = to_s[c_idx]
            if from_c not in trans:
                trans[from_c] = to_c
            else:
                assert(trans[from_c] == to_c)
    for c in string.lowercase:
        if c not in trans.keys():
            for d in string.lowercase:
                if d not in trans.values():
                    trans[c] = d
                    break
    assert(len(trans.keys()) == 27)
    trans_from = []
    trans_to = []
    for c in trans:
        trans_from.append(c)
        trans_to.append(trans[c])
    trans_table = string.maketrans("".join(trans_from), "".join(trans_to))
    for from_s, to_s in strings:
        assert(string.translate(from_s, trans_table) == to_s)
    
    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        s = rl()
        s.strip()
        answer = solver(s, trans_table)
        output.append('Case #%d: %s' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
