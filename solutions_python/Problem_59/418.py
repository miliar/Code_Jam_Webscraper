# http://networkx.lanl.gov/download.html
import networkx as nx
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = open("A-large.in", "r")
# input_file = open("sample.in", "r")
output_file = open("output.txt", "w")

T = int(input_file.readline())

for i in xrange(T):

    N, M = map(int, input_file.readline().split(" "))

    dirs = []
    newdirs = []

    for j in xrange(N):
        line = input_file.readline().strip()
        line = line.split("/")
        line.pop(0)
        dirs.append(line)

    for j in xrange(M):
        line = input_file.readline().strip()
        line = line.split("/")
        line.pop(0)
        newdirs.append(line)

    totmkdirs = 0

    for newdir in newdirs:
        mkdirs = len(newdir)
        for ddir in dirs:
            tot = len(newdir)
            if len(ddir) > len(newdir):
                loop = len(newdir)
            else:
                loop = len(ddir)

            for j in xrange(loop):
                if ddir[j] == newdir[j]:
                    tot = tot - 1
                else:
                    break

            if tot < mkdirs:
                mkdirs = tot

        totmkdirs = totmkdirs + mkdirs
        dirs.append(newdir)

    result = "Case #%s: %s" % (i + 1, totmkdirs)

    print result
    print >> output_file, result

input_file.close()
output_file.close()