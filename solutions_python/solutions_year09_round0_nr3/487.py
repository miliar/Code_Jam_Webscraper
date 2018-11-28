import fileinput
from collections import defaultdict

TARGET_STRING = "welcome to code jam"
INDEXED_TARGET = list(enumerate(TARGET_STRING))
TARGET_OFFSET_DICT = defaultdict(list)
for x in INDEXED_TARGET:
    TARGET_OFFSET_DICT[x[1]].append(x[0])

def countPossibilities(source):
    counters = [0] * (len(TARGET_STRING)+1)
    counters[0] = 1
    for c in source:
        if c in TARGET_OFFSET_DICT:
            offsets = TARGET_OFFSET_DICT[c]
            #print "Counting char",c,"at offset",offsets,"current counts:",counters
            for x in sorted(offsets):
                counters[x+1] += counters[x]
    return counters[-1]

def main():
    it = fileinput.input()
    it.next()
    for idx,l in enumerate(it):
        print "Case #%d: %04d" % (idx+1, countPossibilities(l) % 10000)

if __name__ == "__main__":
    main()
