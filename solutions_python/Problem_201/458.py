def problem(inPath, outDir = ""):
    def solve(inPath, processor, outDir = ""):
        from multiprocessing import Pool
        from os import path

        inf = open(inPath, 'rU')
        stem = path.basename(inPath)
        name, extension = path.splitext(stem)
        outName = name + ".out"
        outPath = path.join(outDir, outName)
        outf = open(outPath, 'w')

        inf.readline() #discard the line which tells us how many lines of input there are
        pool = Pool()
        outputs = pool.map(processor, (line.strip() for line in inf))
        for i, result in enumerate(outputs, 1):
            string = "Case #%s: %s" % (i, result)
            if i > 1:
                outf.write("\n")
            outf.write(string)

    solve(inPath, processor, outDir)

def processor(string):
    n, k = map(int, string.split())
    return "{} {}".format(*answer(n, k))

CACHE = {}

def answer(n, k):
    return combined(n, k)

def splitStalls(n):
    """Splits an integer, n, into two integers, m and M, such that:
1. 0 <= M - m <= 1
2. m + M + 1 == n"""
    
    evened = n + (n % 2)
    midpoint = evened//2
    left = midpoint - 1
    right = n - midpoint
    lower, higher = sorted((left, right))
    return (lower, higher)

def combined(n, k):
    from collections import defaultdict
    gaps = defaultdict(int)
    gaps[n] = 1
    remaining = k
    while remaining > 0:
        ordered = sorted(gaps.keys())
        largest = ordered[-1]
        count = gaps[largest]
        remaining -= count
        del gaps[largest]
        m, M = splitStalls(largest)
        gaps[m] += count
        gaps[M] += count
    return (M, m)
