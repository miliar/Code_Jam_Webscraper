# python file_fix_it.py input_file output_file
import sys

def count_mkdirs(exist, want):
    exset = set()
    for ex in exist:
        parts = ex.split('/')[1:]
        path = parts[0]
        exset.add(path)
        for i in range(1, len(parts)):
            path += '/%s' % parts[i]
            exset.add(path)
    initSize = len(exset)

    for ex in want:
        parts = ex.split('/')[1:]
        path = parts[0]
        exset.add(path)
        for i in range(1, len(parts)):
            path += '/%s' % parts[i]
            exset.add(path)

    return len(exset) - initSize
        

inpath = sys.argv[1]
outpath = sys.argv[2]
fin = open(inpath)
fout = open(outpath, 'w')
T = int(fin.readline().strip())
for i in range(T):
    N, M = (int(s) for s in fin.readline().strip().split())
    exist = [fin.readline().strip() for j in range(N)]
    want = [fin.readline().strip() for j in range(M)]
    count = count_mkdirs(exist, want)
    print >>fout, 'Case #%d: %d' % (i+1, count)
fout.close()
