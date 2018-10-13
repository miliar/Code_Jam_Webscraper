import sys

def count_mkdirs(paths, newpaths):
    # create starting dir structure
    dirs = {'':{}}
    for p in paths:
        parts = p.split('/')
        cdir = dirs
        for part in parts:
            if part not in cdir:
                cdir[part] = {}
            cdir = cdir[part]
    # print dirs

    # do any needed mkdirs
    count = 0
    for p in newpaths:
        parts = p.split('/')
        cdir = dirs
        for part in parts:
            if part not in cdir:
                cdir[part] = {}
                count += 1
                # print 'made dir ' + part
                # print dirs
            cdir = cdir[part]

    return count

def solve(inpath, outpath):
    infile = open(inpath, 'r')
    outfile = open(outpath, 'w')
    casecount = int(infile.readline())
    for i in xrange(1, casecount + 1):
        numdirs, numnewdirs = map(int, infile.readline().split(' '))
        dirs = []
        for j in xrange(1, numdirs + 1):
            dirs.append(infile.readline().strip())
        newdirs = []
        for j in xrange(1, numnewdirs + 1):
            newdirs.append(infile.readline().strip())
        output = 'Case #%d: %d' % (i,
            count_mkdirs(dirs, newdirs)
            )
        print output
        outfile.write(output + '\n')
    return

if __name__ == "__main__":
    inpath = sys.argv[1]
    outpath = sys.argv[2]
    solve(inpath, outpath)