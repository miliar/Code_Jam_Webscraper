from itertools import combinations

def add(a, b):
    b1, b2 = bin(a)[2:], bin(b)[2:]
    if len(b1) < len(b2):
        b1 = '0' * (len(b2) - len(b1)) + b1
    elif len(b2) < len(b1):
        b2 = '0' * (len(b1) - len(b2)) + b2
    
    digits = zip(b1, b2)
    
    result = ''
    
    for d1, d2 in digits:
        s = int(d1) + int(d2)
        if s == 2:
            s = 0
        result += str(s)
    
    return int(result, 2)


def mysum(l):
    return reduce(add, l)

    
def sub(a, b):
    c = list(a)
    for i in b:
        c.remove(i)
    return c


def find(seq):
    seq = sorted(seq)
    found = None
    for i in xrange(1, len(seq) / 2 + 1):
        for subseq in combinations(seq, i):
            other_subseq = tuple(sub(seq, subseq))
            if mysum(subseq) == mysum(other_subseq):
                found = max([sum(subseq), sum(other_subseq)])
                break
        if found:
            break
    return found


fin = open('C-small-attempt1.in')
fout = open('candy.out', 'w')


cases = int(fin.readline())

for case_index in range(cases):
    number = int(fin.readline())
    seq = map(int, fin.readline().strip().split()[:number])
    result = find(seq)
    if result is None:
        result = 'NO'
    else:
        result = str(result)
    fout.write('Case #%d: %s\n' % (case_index + 1, result))


fin.close()
fout.close()


