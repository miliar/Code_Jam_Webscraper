import sys
from string import maketrans

tr_table = ''

def train():
    tr_dict = {}
    orig = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv',
        'y qee',
        'z']
    trans = ['our language is impossible to understand',
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up',
        'a zoo',
        'q']
    for o, t in zip(orig, trans):
        for lo, lt in zip(o, t):
            tr_dict[lo] = lt
    global tr_table
    tr_table = maketrans(str(tr_dict.keys()), str(tr_dict.values()))
    

def main():
    with sys.stdin as f:
        for x in range(int(f.readline())):
            solve(f, x+1)

def solve(f, case):
    strin = f.readline()
    global tr_table
    strout = strin.translate(tr_table, '\n')
    print 'Case #%d: %s' % (case, strout)

if __name__ == '__main__':
    train()
    main()
