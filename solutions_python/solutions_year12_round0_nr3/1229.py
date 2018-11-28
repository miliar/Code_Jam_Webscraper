def is_recycled(a, b):
    a = str(a)
    b = str(b)
    for i in xrange(len(a)):
        index = b.rfind(a[:i])
        if index == -1:
            continue
        if b[:index] == a[i:] :
            return 1
    return 0

def main(input_path, output_path):
    infile = open(input_path)
    outfile = open(output_path, 'wt')
    cases = int(infile.readline())
    for case_number in xrange(1, cases + 1):
        case = infile.readline()
        start = int(case.split()[0])
        end = int(case.split()[1])
        recycled = 0
        for m in xrange(start, end + 1):
            for n in xrange(start, m):
                recycled += is_recycled(n, m)
        outfile.write("Case #%d: %d\n" % (case_number, recycled))
    infile.close()
    outfile.close()

if __name__ == "__main__":
    import sys
    import time
    start = time.time()
    main(*sys.argv[1:])
    print time.time() - start
