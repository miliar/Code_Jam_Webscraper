from collections import defaultdict
import time
from pprint import pprint

with file("A-large-0.in") as inp:
    with file("A-large-0.out", "w") as outp:
        full = int(inp.readline().strip())
        for casen in xrange(full):
            r, c = [int(x) for x in inp.readline().strip().split()]
            mtx = [[x for x in inp.readline().strip()]
                   for y in xrange(r)]
            impossible = False
            while True:
                found = False
                for y in xrange(r):
                    broken = False
                    for x in xrange(c):
                        if mtx[y][x] == "#":
                            found = True
                            if (y < r - 1 and
                                x < c - 1 and
                                mtx[y][x+1] == "#" and
                                mtx[y+1][x] == "#" and
                                mtx[y+1][x+1] == "#"):
                                mtx[y][x] = "/"
                                mtx[y][x+1] = "\\"
                                mtx[y+1][x] = "\\"
                                mtx[y+1][x+1] = "/"
                                broken = True
                                break
                            else:
                                impossible = True
                                break
                    if broken or impossible:
                        break

                #pprint(mtx)
                #time.sleep(1)
                if impossible or not found:
                    break
            outp.write("Case #%s:\n" % (casen + 1))
            if impossible:
                outp.write("Impossible\n")
            else:
                for row in mtx:
                    outp.write("%s\n" % "".join(row))

