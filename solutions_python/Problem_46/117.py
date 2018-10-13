import re
import sys

from itertools import izip

input = sys.stdin
#input = open('A-small-attempt0.in')

cache = {}
all_cache = set()

def ri(fp=input): # readint
    return ris(1, fp)[0]

def ris(n, fp=input):  # readints
    return map(int, fp.readline().split())

def rl(fp=input):
    return input.readline().strip()

def read_case():
    N = ri()
    matrix = [rl() for i in range(N)]

    return [matrix]

def good(matrix, tr):
    matrix = gen_transp(matrix, tr)

    for i, row in enumerate(matrix):
        if '1' in set(row[i+1:]):
            return False
    return True

def gen_transp(matrix, indices):
    return [matrix[i] for i in indices]

def get_transp(tr):
    res = []
    for j in range(len(tr)-1):
        m2 = tr[:]
        m2[j], m2[j+1] = tr[j+1], tr[j]
        res.append( m2)
    return res

def iterate_transp(level=0):
    res = []
    cache[level+1] = {}
    for j in cache[level].values(): # precompute next layer
        for v in j:
            children = [x for x in get_transp(v) if str(x) not in all_cache]
            cache[level+1][str(v)] = children
            all_cache.update(map(str, children))
            res.append(v)
    return res


def process_case(matrix):
    global cache, all_cache

    tr = range(len(matrix))
    cache = {0: {str(tr): get_transp(tr)}}
    all_cache = set()

    if good(matrix, tr):
        return 0
    i = 0
    while True:
        for tr in iterate_transp(i):
            if good(matrix, tr):
                return i + 1
        i +=1

def main():
    T = ri()
    for i, test_case in enumerate(range(T)):
        case = read_case()
        res = process_case(*case)
        print "Case #%d: %s" % (i + 1, res)


if __name__ == '__main__':
    main()
