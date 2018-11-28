import re, sys

def main(fname):
    f = file(fname)
    l, d, n = map(int, f.readline().split())
    words = []
    for i in range(0, d):
        words.append(f.readline().strip())
#    print words
    for i in range(0, n):
        testline = f.readline().strip()
        regex = testline.replace("(", "[").replace(")", "]")
        pat = re.compile(regex)
        cnt = 0
        for w in words:
            if pat.match(w):
                cnt += 1
        print "Case #%d: %d" % (i+1, cnt)

if __name__ == '__main__':
    main(sys.argv[1])
