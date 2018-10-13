#!/bin/python
import sys

decodeMap = { }
for x, y in zip("ejpmysljylckdkxveddknmcrejsicpdrysi",
                "ourlanguageisimpossibletounderstand"):
    decodeMap[x] = y
for x, y in zip("rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd",
                "therearetwentysixfactorialpossibilities"):
    decodeMap[x] = y
for x, y in zip("dekrkdeoyakwaejtysrreujdrlkgcjv",
                "soitisokayifyouwanttojustgiveup"):
    decodeMap[x] = y

num_tests = int(sys.stdin.readline())
decodeMap['q'] = 'z'
#decodeMap['b'] = 'q'
decodeMap['z'] = 'q'
decodeMap[' '] = ' '
#print sorted("".join(map(lambda (x, y): y, decodeMap.items())))
for test in range(num_tests):
    text = sys.stdin.readline().strip()
    ans = ""
    for c in text:
        ans = ans + str(decodeMap[c])
    print "Case #%d: %s" % (test + 1, ans)
