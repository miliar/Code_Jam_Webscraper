import re

def main():
    L,D,N = map(int,raw_input().split())
    d = [raw_input() for _ in range(D)]
    for n in range(1,N+1):
        print 'Case #%s: %s' % (n,f(d,raw_input()))
    #print L,D,N,d

r = re.compile(r'\((\w+)\)')
def make_re(s):
    return r.sub(
        lambda g: r'(%s)' % '|'.join(g.group(1)), 
        s)

def f(d,s):
    #print make_re(s)
    r_ = re.compile(make_re(s))
    return sum(1 for w in d if r_.match(w))

###
import random,string

def rand_string(l):
    return ''.join(random.choice(string.lowercase)
                   for _ in xrange(l))

if __name__ == '__main__':
    main()
