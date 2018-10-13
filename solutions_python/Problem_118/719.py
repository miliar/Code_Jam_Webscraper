import sys
from math import *
from itertools import *

WAIT_TOTAL = 0
WAIT_CASE = 1

ga = None

def process_input():

    cases_count = 0

    state = WAIT_TOTAL
    for line in sys.stdin.readlines():
        line = line.strip()
        if line != '':

            if state == WAIT_TOTAL:
                c = int(line)
                state = WAIT_CASE
            elif state == WAIT_CASE:
                cases_count += 1
                assert cases_count <= c
                (A,B) = line.split(' ')
                (A,B) = (long(A), long(B))
                ret = process_case(A,B)
                sys.stdout.write('Case #' + str(cases_count) + ': ')
                print ret
            else:
                assert False


def process_case(a,b):
    try:
        return len(list(takewhile(lambda x: x <= b, dropwhile(lambda x: x < a, ga))))
    except:
        return 0
    #return len(list(gen_all(a,b)))

def process_case2(a,b):

    #a = get_first(a,b)
    b = get_last(a,b)

    ret = xrange(a,b+1)
    print 'a'
    ret = ifilter(lambda x: palindrome(x), ret)
    ret,dbg = tee(ret,2)
    print 'b', list(islice(dbg,0,10))
    ret = imap(lambda x: x*x, ret)
    ret,dbg = tee(ret,2)
    print 'c', list(islice(dbg,0,10))
    ret = ifilter(lambda x: palindrome(x), ret)
    ret,dbg = tee(ret,2)
    print 'd', list(islice(dbg,0,10))
    l = list(ret)
    print 'l:',l
    return len(l)

def get_last(x,y):
    possible()

    ret = xrange(4004009004006,x+1,-2)
    ret,dbg = tee(ret,2)
    print 'al', list(islice(dbg,0,5))
    ret = ifilter(lambda x: palindrome(x), ret)
    ret,dbg = tee(ret,2)
    print 'bl', list(islice(dbg,0,5))
    ret = ifilter(lambda x: is_square(x), ret)
    ret,dbg = tee(ret,2)
    print 'bl2', list(islice(dbg,0,5))
    ret = imap(lambda x: sqrt(x), ret)
    ret,dbg = tee(ret,2)
    print 'cl', list(islice(dbg,0,5))
    ret = ifilter(lambda x: palindrome(x), ret)
    ret,dbg = tee(ret,2)
    print 'dl', list(islice(dbg,0,5))
    last = ret.next()
    print 'l:',last
    return last

xrange = lambda start,stop: iter(count(start).next, stop)

# start is supposed to be valid (1)
def possible(start,end):
    yield start
    while True:
        a = start + long(sqrt(start))
        b = end * end
        ret = xrange(a,b)
        #ret = ifilter(lambda x: palindrome(x), ret)
        ret = imap(lambda x: (x,x*x), ret)
        ret = ifilter(lambda x: palindrome(x[1]), ret)
        start = ret.next()
        if start[1] >= end:
            return
        to_yield = start[1]
        start = start[0]
        yield to_yield

def gen_all(start,end):
    a = start
    b = end
    ret = imap(lambda x: x*x, palindromes_gen())
    ret = takewhile(lambda x: x <= b, dropwhile(lambda x: x < a, ret))
    ret = ifilter(lambda x: palindrome(x), ret)
    while True:
        n = next(ret)
        #print n, ', '
        yield n


# start is supposed to be valid (1)
def possible_rev(start,end):
    yield start
    while True:
        a = start - long(sqrt(start))
        ret = xrange(a,end,-1)
        ret = ifilter(lambda x: palindrome(x), ret)
        ret = ifilter(lambda x: is_square(x), ret)
        ret = imap(lambda x: sqrt(x), ret)
        ret = ifilter(lambda x: palindrome(x), ret)
        start = ret.next()
        yield start

def palindromes_gen_1_digit():
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9

def palindromes_gen_2_digit():
    yield 00
    yield 11
    yield 22
    yield 33
    yield 44
    yield 55
    yield 66
    yield 77
    yield 88
    yield 99

# start is supposed to be valid (1)
def palindromes_gen():
    one = palindromes_gen_1_digit()
    two = islice(palindromes_gen_2_digit(),1,10)
    digit = 3
    q = palindromes_gen_digits(digit)
    p = chain(one,two,q)
    while True:
        try:
            n = next(p)
            yield n
        except:
            digit += 1
            p = palindromes_gen_digits(digit)

def palindromes_gen_digits(x):
    if x == 1:
        g = palindromes_gen_1_digit()
        while True:
            try:
                yield next(g)
            except:
                return
    if x == 2:
        g = palindromes_gen_2_digit()
        while True:
            try:
                yield next(g)
            except:
                return
    a = 2 if x % 2 == 0 else 1
    prev_digits = range(a,x,2)
    prev_gens = [palindromes_gen_digits(i) for i in prev_digits]
    prev_gen = chain(*prev_gens)
    p = palindromes_gen_1_digit()
    p.next() # Skip 0
    while True:
        n = p.next()
        #print 'n',n
        exit = False
        while not exit:
            try:
                m = prev_gen.next()
                #print 'm',m
                if m == 0:
                    m_str = '0'*(x-2)
                else:
                    m_str = str(m)
                while len(m_str) < x-2:
                    m_str = '0' + m_str + '0'
                yield long(str(n)+m_str+str(n))
            except:
                exit = True
                prev_gens = [palindromes_gen_digits(i) for i in prev_digits]
                prev_gen = chain(*prev_gens)

def repeat_each(gen,times):
    g = iter(gen)
    while True:
        try:
            e = next(gen)
        except:
            return
        for i in xrange(0,times):
            yield e
            
def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

# start is supposed to be valid (1)
def palindromes_gen2():
    first = palindromes_gen_base
    first, first2 = tee(first)
    reflexed = imap(lambda x: long(str(x)+str(x)), first2)
    ret = chain(first, reflexed)
    return ret

# start is supposed to be valid (1)
def palindromes_gen_base():
    first = xrange(1,9+1)
    first, first2 = tee(first)
    reflexed = imap(lambda x: long(str(x)+str(x)), first2)
    ret = chain(first, reflexed)
    return ret

def is_square(apositiveint):
    x = apositiveint // 2
    seen = [x]
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: 
            return False
        else:
            seen.append(x)
    return True

def palindrome(x):
    n = x
    rev = 0
    while x > 0:
        dig = x % 10
        rev = rev * 10 + dig
        x = x / 10
    return n == rev

def palindrome2(x):
    x = str(x)
    if len(x) <= 1:
        return True
    if len(x) % 2 == 0:
        #print x[:len(x)/2] , x[len(x)/2:]
        return x[:len(x)/2] == ''.join(list(reversed(x[len(x)/2:])))
    else:
        #print x[:len(x)/2] , x[len(x)/2+1:]
        return x[:len(x)/2] == ''.join(list(reversed(x[len(x)/2+1:])))


if __name__ == '__main__':
    #for i in gen_all(0, pow(10,30) ):
    #    #sys.stdout.write(str(i) + ', ')
    #    print i, ', '
    #print ''

    ga = list(gen_all(0, pow(10,14)))

    process_input()


