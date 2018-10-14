
from itertools import combinations

def get_line():
    return raw_input().strip()

formatIntegerList = lambda s: list(map(int,s.split(' ')))

def standard_input():
    T = int(get_line())
    for i in range(T):
        lst = formatIntegerList(get_line())
        M, N = lst[0], lst[1]
        strs = []
        for j in range(M):
            strs.append(get_line())
        yield (i+1,(M,N,strs))
        
def partition(strs, N):
    if N == 1:
        yield [strs]
    elif len(strs) == 0:
        for p in partition(strs, N - 1):
            yield [strs] + p
    else:
        for r in range(0,len(strs) + 1):
            for ite in combinations(strs, r):
                site = set(ite)
                for p in partition(strs - site, N - 1):
                    yield [site] + p
                    
def sizeoftries(part):
    result = 0
    for strset in part:
        preset = set()
        for s in strset:
            for i in range(0, len(s) + 1):
                preset |= set([s[:i]])
        result += len(preset)
    return result
     
def handle_case(case):
    M, N,strs = case
    strs = set(strs)
    maxsize = 0
    result = 0
    for part in partition(strs, N):
        s = sizeoftries(part)
        # print s, part
        if s == maxsize:
            result += 1
        elif s > maxsize:
            result = 1
            maxsize = s
    return "%d %d" % (maxsize, result)
    
        
def main():
    for i,case in standard_input():
        print "Case #%d: %s" %(i,handle_case(case))        

if __name__ == '__main__':
    main()
    