import string

GOOGLE = 'z y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
ENGLISH = 'q a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

def solve(filename, out_filename):
    trans = string.maketrans(GOOGLE, ENGLISH)
    print trans[97:123]
    for c in string.ascii_lowercase:
        if c not in ENGLISH:
            print c
    with open(filename) as in_file:
        with open(out_filename, 'wb') as out_file:
            cases = int(in_file.next().strip())
            for i in xrange(cases):
                line = in_file.next().strip()
                out_file.write('Case #%d: %s\r\n' % (i+1, line.translate(trans)))

if __name__ == '__main__':
    solve('A-small-attempt1.in', 'A-small-attempt0.out.txt')
    
