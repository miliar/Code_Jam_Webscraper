import sys
import itertools
import math
import collections
import functools

def read_word(f):
    return next(f).strip()
def read_int(f, b=10):
    return int(read_word(f), b)
def read_letters(f):
    return list(read_word(f))
def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]
def read_words(f, d=' '):
    return read_word(f).split(d)
def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]
def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]
def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res
def solve(solver,SMALL=True,PRACTICE=False):
    fn = sys.argv[0]
    fn = fn[ 1+fn.rfind('/'): fn.rfind('.') ]
    fn = fn+['-large','-small'][SMALL]+['','-practice'][PRACTICE]
    in_fn = fn + '.in'
    out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                print i+1, res
                write_case(fo, i+1, res)
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

#######################################################

def read_case(f):
    N,X = read_ints(f)
    A = read_ints(f)
    return N,X,A

#######################################################
def binary_search_le(a, x, lo=0, hi=None):   #largest that is <= x
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    #print lo, hi, '1'
    try:
        if a[lo-1] <= x: return lo-1
    except:
        pass
    return -1

def solver(case):
    N,X,A = case
    
    A.sort()
    #print A
    ct = 0
    mask = [True for i in xrange(N)]
    for i in xrange(N-1,-1,-1):

        if mask[i]:
            mask[i] = False
            p= binary_search_le(A,X-A[i])
            try:
                while not mask[p]:
                    p -= 1
                    if p == 0: break
                if p > -1: mask[p] = False
            except:
                #print N,X,A, '##'
                #print i, p, 'hi'
                pass
            
            
            #print mask
            ct += 1
    print 'ans',ct
    return ct

#False for large
solve(solver,True)
#solve(solver,False)

print 'Done'
