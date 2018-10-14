import sys
import cPickle

import psyco
psyco.full()

def get_all_rotations(string):
    #rots = []
    
    #for x in range(len(string)):
    #    rots.append(''.join((s[x:], s[:x])))
    
    return [''.join((string[x:], string[:x])) for x in range(len(string))]


def get_n_pairs(n, B):
    pairs = []
    #pairs = 0
    
    n_str = str(n)
    
    for m_str in get_all_rotations(n_str):
        if m_str[0] == '0':
            continue
        
        m_int = int(m_str)
        
        if n < m_int <= B:
            pairs.append((n, m_int))
            #pairs += 1
    
    return pairs


def get_all_pairs(A, B):
    all_pairs = set()
    #all_pairs = 0
    
    for n in range(A, B+1):
        all_pairs.update(get_n_pairs(n, B))
        #all_pairs += get_n_pairs(n, B)
    
    return all_pairs


#all_pairs = get_all_pairs(0, 2000000)
all_pairs = cPickle.load(open('all_pairs_pickled', 'r'))
# picking only saves a few seconds

#cPickle.dump(all_pairs, open('all_pairs_pickled', 'w'))
#sys.exit()

num_testcases = int(sys.stdin.readline())

for testcase in range(1, num_testcases+1):
    A, B = [int(x) for x in sys.stdin.readline().split()]
    
    count = 0
    for n,m in all_pairs:
        if A <= n < m <= B:
            count += 1
    
    num_pairs = count
    
    #num_pairs = len(get_all_pairs(A, B))
    #num_pairs = get_all_pairs(A, B)
    
    print 'Case #%s: %s' % (testcase, num_pairs)
















