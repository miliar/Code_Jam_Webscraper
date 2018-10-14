import sys;

def main():
    argv = sys.argv[1:]
    if len(argv) < 2:
        print 'Usage: a.py inputfile outputfile'
        sys.exit(1)
    inputFile = open(argv[0],'rU')
    testCases = int(inputFile.readline().strip())
    result = []
    mstr = 'ay bh ce ds eo fc gv hx id ju ki lg ml nb ok pr qz rt sn tw uj vp wf xm ya zq'.split()
    tmap = {}
    for m in mstr:
        tmap[m[0]] = m[-1]
    for testCase in range(testCases):
        ln = inputFile.readline().strip()
        oln = []
        for c in ln:
            if c not in tmap:
                oln.append(c)
            else:
                oln.append(tmap[c])
        result.append('Case #%d: %s\n' % (testCase+1,''.join(oln)))
    outputFile = open(argv[1], 'w')
    outputFile.writelines(result)
    inputFile.close()
    outputFile.close()

if __name__ == '__main__':
    main()
