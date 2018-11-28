import sys

def read_file(filepath):
    try:
        lines = file(filepath, 'rU').readlines()
    except IOError, e:
        print '*** file open failed:', filepath
        raise e
    else:
        return lines

def get_product(v1, v2):
    sum = 0
    for a, b in zip(v1, v2):
        sum += a*b
    return sum

def get_permutation(p):
    if len(p)==1:
        return [p]
    
    answers = []
    for first in p:
        a = [first]
        p2 = p[:]
        p2.remove(first)
        #print 'p2:', p2
        b = get_permutation(p2)
        #print 'b:', b
        for v in b:
            v = a+v
            #print 'v:', v
            answers.append(v[:])    
        #return b
    
    return answers
    
def get_min(v1, v2, per):
    min = sys.maxint
    for p in per:
        v = []
        for i in p:
            v.append(v2[i])
        product = get_product(v1, v)
        if product<min:
            min = product
    
    return min
    
# main
lines = read_file('./A-small-attempt0.in')
for i in range(len(lines)):
    lines[i] = lines[i].rstrip('\r\n')
print lines

T = int(lines[0])
answers = []
i = 1
for m in range(T):
    # read a case
    print 'case #'+str(m+1)+':'
    n = int(lines[i])
    i += 1
    v1 = [int(v) for v in lines[i].split(' ')]
    i += 1
    v2 = [int(v) for v in lines[i].split(' ')]
    i += 1
    print 'v1:', v1
    print 'v2:', v2
    if not len(v1)==n or not len(v2)==n:
        print 'n:', n
        print 'v1 length:', len(v1)
        print 'v2 length:', len(v2)
        exit(1)
        
    # permutate
    p = [v for v in range(n)]
    #print p
    per = get_permutation(p)
    #print 'per:', per
    min = get_min(v1, v2, per)
    
    answers.append(min)
    
    
# answers
for m in range(T):
    print 'Case #'+str(m+1)+':', answers[m]

