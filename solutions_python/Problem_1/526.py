import sys

def solve(engines, queries):
    baseEngines = engines[:]
    s = 0
    for q in queries:
        if len(engines) == 1 and q == engines[0]:
            engines = baseEngines[:]
            s += 1
                
        if q in engines:
            engines.remove(q)
    return s

def main():
    n = int(sys.stdin.readline())
    for i in range(1, n + 1):  
        numEngines = int(sys.stdin.readline())
        engines = [sys.stdin.readline().strip() for j in range(numEngines)]
        numQueries = int(sys.stdin.readline())
        queries = [sys.stdin.readline().strip() for j in range(numQueries)]
        print 'Case #%d: %d' % (i, solve(engines, queries))

if __name__ == '__main__':
    main()
