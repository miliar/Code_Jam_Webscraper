import sys
from collections import deque

A = None
B = None

already_seen = {}

def is_ok(n, m):
    global A
    global B
    global already_seen
    strn = ''.join(n) # need a hashable representation
    if (m[0] == '0' #or  n[0] == '0' # it is not possbile that n[0] == '0'
        or n > m
        or m > B): 
        return False
    elif n == m:
        already_seen[strn] = True
        return False
    elif strn in already_seen:
        return False
    else:
        return True

def num_rec_pairs(int_n):
    global A
    global B
    # assume n is in the proper range
    res = 0;
    n = deque(str(int_n))
    m = deque(n) # copy of n
    for _ in range(len(n)-1):
        m.rotate()
        if is_ok(n,m):
            res += 1
            #print (''.join(n), ''.join(m))
    
    return res

def answer(test):
    global A
    global B
    A, B = tuple(deque(n) for n in test.split(' '))
    intA, intB = int(''.join(A)), int(''.join(B))
    rec_pairs = 0
    for n in range(intA,intB+1):
        rec_pairs += num_rec_pairs(n)
    return rec_pairs

with open(sys.argv[1]) as f:
    with open('output','w') as out:
        for i, test in enumerate(f):
            if i == 0: 
                continue
            out.write("Case #%i: %i\n" % (i, answer(test)))
            #sys.stdout.write("Case #%i: %i\n" % (i, answer(test)))

print len(already_seen)
