import sys

def readlines(f):
    num_lines = f.readline()
    for line in f:
        yield line[:-1]

def create_cases(lines):
    for line in lines:
        l = [int(num) for num in line.split(' ')]
        N, S, p, ts = l[0], l[1], l[2], l[3:]
        yield S, p, ts

def case_results(cases):
    def surprise_pairs(n):
        for s1 in range(n):
            for s2 in range(s1 + 1, n):
                yield s1, s2
    
    def best_surprising_result(t, p):
        for b in range(10, 1, -1):
            if sum([b, b, b-2]) == t or sum([b, b-1, b-2]) == t or sum([b, b-2, b-2]) == t:
                return 1 if b >= p else 0
        
        return None
    
    def best_unsurprising_result(t, p):
        for b in range(10, 0, -1):
            if sum([b, b, b]) == t or sum([b, b, b-1]) == t or sum([b, b-1, b-1]) == t:
                return 1 if b >= p else 0
        
        assert t == 0
        return 1 if p == 0 else 0
    
    def result_sets(S, p, ts):
        indices = range(len(ts))
        bs = [best_surprising_result(t, p) for t in ts]
        bu = [best_unsurprising_result(t, p) for t in ts]
        bu_result = sum(bu)
        
        if S == 0:
            yield bu_result
        elif S == 1:
            for s in indices:
                if bs[s] is not None:
                    yield bu_result - bu[s] + bs[s]
        else:
            for s1, s2 in surprise_pairs(len(ts)):
                if bs[s1] is not None and bs[s2] is not None:
                    yield bu_result - bu[s1] - bu[s2] + bs[s1] + bs[s2]
    
    def case_result(S, p, ts):
        return max(result_sets(S, p, ts))
    
    for case in cases:
        yield case_result(*case)

def output(results):
    for i, o in enumerate(results):
        print 'Case #{i}: {o}'.format(i=i+1, o=o)

def run():
    in_lines = readlines(sys.stdin)
    cases = create_cases(in_lines)
    results = case_results(cases)
    output(results)

if __name__ == '__main__':
    run()
