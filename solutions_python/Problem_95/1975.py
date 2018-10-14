import string
import sys
from itertools import izip

def main(args):
    assert len(args) == 2, 'args length != 2: args was %s' % args
    fname = args[1]
    infile = '%s.in' % fname
    outfile = '%s.out' % fname
    
    coded = (
        'eqyz',
        'ejp mysljylc kd kxveddknmc re jsicpdrysi',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv',
        )
    plaintext = (
        'ozaq',
        'our language is impossible to understand',
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up',
        )

    trans_dict = dict()
    for code, plain in izip(coded, plaintext):
        for i, char in enumerate(code):
            if char in trans_dict:
                assert trans_dict[char] == plain[i]
            elif char.isalpha():
                trans_dict[char] = plain[i]

    from_chararray = []
    to_chararray = []
    for from_, to_ in sorted(trans_dict.iteritems()):
        from_chararray.append(from_)
        to_chararray.append(to_)
    translation_table = string.maketrans(
        ''.join(from_chararray),
        ''.join(to_chararray),
        )

    print len(''.join(from_chararray).translate(translation_table))

    # for code_string in coded:
    #     print code_string.translate(translation_table)

    with open(infile, 'r') as f, open(outfile, 'w') as g:
        num_tests = int(f.readline().strip())
        for i in xrange(1, num_tests+1):
            coded_string = f.readline().strip()
            result = coded_string.translate(translation_table)
            g.write('Case #%s: %s\n' % (i, result))
    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)
