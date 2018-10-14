import csv
import itertools

def jam(filename, mapper, num_args):
   " Generic helper to process Google Code Jam input file "
   with open(filename, 'rb') as f:
       reader = csv.reader(f)
       N = int(reader.next()[0])
       c = 0
       for arg0 in reader:
           c += 1
           args = arg0 + [reader.next() for _ in range(1, num_args)]
           yield mapper(*args)
       assert N == c, "Expected %s cases but found only %s" % (N, c)

def get_recycles_for_int(i):
    assert type(i) == int
    def get_cycles(s, acc=[]):
        if len(acc) < len(s):
            acc.append(s)
            t = s[-1] + s[:-1]
            return get_cycles(t, acc)
        else:
            return acc
    return list(set([
        int(c) for c in get_cycles(str(i))
        if int(c) > i and
        not c.startswith('0')
        ]))

# precompute        
d = dict((i, get_recycles_for_int(i)) for i in range(2000001))
print 'precompute ok'

def process(arg0):
    A, B = map(int, arg0.split())
    c = 0
    for k in range(A, B+1):
        c += len(filter(lambda x: x <= B, d[k]))
        #print filter(lambda x: x < B, d[k])
    return c

with open('C.out', 'wb') as f:
    for i, r in enumerate(jam('C.in', process, 1)):
        response = "Case #%s: %s" % (i+1, r)
        print response
        f.write(response)
        f.write('\n')






