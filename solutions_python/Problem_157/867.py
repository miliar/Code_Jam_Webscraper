
import csv
import itertools
import copy
import time


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        L, X = csv_r.next()
        v = csv_r.next()
        test_lst.append([int(L), int(X), v])
    f.close() 
    return test_lst 


d = {('1','1') : '1',('1','i') : 'i' , ('1','j') : 'j' , ('1','k') : 'k',
     ('i','1') : 'i',('i','i') : '-1', ('i','j') : 'k' , ('i','k') : '-j',
     ('j','1') : 'j',('j','i') : '-k', ('j','j') : '-1', ('j','k') : 'i',
     ('k','1') : 'k',('k','i') : 'j' , ('k','j') : '-i', ('k','k') : '-1',
    }

dres = {'-1' : (-1, '1'),
        '-i' : (-1, 'i'),
        '-j' : (-1, 'j'),
        '-k' : (-1, 'k'),
       }
 
def multiply(a, b):
   global loc_mnemo_dct
   if (a, b) not in loc_mnemo_dct:
        sa = 1 if '-' not in a else -1
        sb = 1 if '-' not in b else -1
        res = d[(a.replace('-', ''), b.replace('-', ''))]
        sres = sa*sb*(1 if '-' not in res else -1)
        to_return = ('' if sres == 1 else '-') + res.replace('-', '')
        loc_mnemo_dct[(a,b)] = to_return
   return loc_mnemo_dct[(a,b)]


def explore(s):
    global mnemo_dct
    if s not in mnemo_dct:
        n = len(s)
        if n == 1:
            to_return = s
        else:
            idx = min(max(1, n/2), len(s)-1)
            left, right = s[:idx], s[idx:]
            to_return = multiply(explore(left), explore(right))
        mnemo_dct[s] = to_return
    return mnemo_dct[s]


def divide(a, b):
    global div_dct
    return div_dct[(a, b)]


def solve_test(test_case):
    L, X, v = test_case
    vv = ''.join(X*v)
    for i in xrange(0, len(vv)-2):
        if i == 0:
            w1 = vv[0]
            w2 = vv[1]
            w3 = explore(vv[2:])
        else:
            w1 = multiply(w1, vv[i])
            w2 = vv[i+1]
            w3 = divide(vv[i+1], w3)
        if w1 != 'i':
            continue
        if w2 == 'j' and w3 =='k':
            return 'YES'
        cur_w2, cur_w3 = w2, w3
        for j in xrange(i+1, len(vv)-1):
            cur_w2 = multiply(cur_w2, vv[j+1])
            cur_w3 = divide(vv[j+1], cur_w3)
            if cur_w2 == 'j' and cur_w3 == 'k':
                return 'YES'
    return "NO"


def check_mul():
    print 'k' == multiply('i', 'j')
    print '-k' == multiply('-i', 'j')
    print 'j' == multiply('-i', 'k')
    print 'j' == multiply('i', '-k')
    print '-k' == multiply('-1', 'k')
    print 'k' == multiply('-1', '-k')
 

def init():
    for a in ['1', 'i', 'j', 'k']:
        for b in ['1', 'i', 'j', 'k']:
            _ = multiply(a, b)
            _ = multiply(a, '-'+b)
            _ = multiply('-'+a, b)
            _ = multiply('-'+a, '-'+b)
    global div_dct
    global loc_mnemo_dct
    div_dct = {}
    for k, v in loc_mnemo_dct.items():
        a, b = k
        div_dct[(a, v)] = b


def main(filename):
    test_lst = read_file(filename)
    global mnemo_dct
    mnemo_dct = {}
    global loc_mnemo_dct
    loc_mnemo_dct = {}
    init()
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case)
        print "Case #%i: %s" % (1+i_test, res)


if __name__ == '__main__':
    #main('./A-large.in')
    #main('./simple.in')
    main('./C-small-attempt2.in')

