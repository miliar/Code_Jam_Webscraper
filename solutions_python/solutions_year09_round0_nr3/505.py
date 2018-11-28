import sys

NEEDLE = "welcome to code jam"
NEEDLE_LENGTH = len(NEEDLE)

def find_str(haystack):
    # We are only looking for substrings.
    if len(haystack) <= NEEDLE_LENGTH: return 0

    # For efficient access to the character positions we're going to store
    # the positions in a map.
    charMap = {}
    for pos, x in enumerate(haystack): charMap.setdefault(x, []).append(pos)

    # If the map doesn't contain all of necessary letters there are no matches.
    for n in NEEDLE:
        if n not in charMap: return 0
    
    def _find(haystack, haystackIndex, needleIndex, charMap):
        # If we reach the end of needle we've found a substring.
        if needleIndex == NEEDLE_LENGTH: return 1
        indexes = (i for i in charMap[NEEDLE[needleIndex]] if i > haystackIndex)
        return sum(_find(haystack, i, needleIndex + 1, charMap) for i in indexes)

    return _find(haystack, -1, 0, charMap)
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: ", sys.argv[0], " <filename>"
        exit()

    try:
        f = open(sys.argv[1])
        f.readline() # The count of cases in the file.
        for index, line in enumerate(f):
            total = find_str(line)
            print "Case #%i:" % (index + 1), ("%04d" % total)[-4:]
        f.close()
    except IOError, e:
        print "While opening input file:", str(e)

