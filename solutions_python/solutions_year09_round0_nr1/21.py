import re, sys

def main():
    (L, D, N) = sys.stdin.readline().split(" ")
    (L, D, N) = (int(L), int(D), int(N))
    wordList = [sys.stdin.readline().rstrip("\n") for i in xrange(D)]
    
    for case in xrange(1, N + 1):
        pat = sys.stdin.readline().rstrip("\n")
        pattern = [str() for i in xrange(L)]
        inside = False
        patIdx = 0
        for i in xrange(len(pat)):
            if pat[i] == '(':
                inside = True
            elif pat[i] == ')':
                inside = False
                patIdx += 1
            else:
                pattern[patIdx] += pat[i]
                if not inside:
                    patIdx += 1
        result = 0
        for i in xrange(D):
            results = [wordList[i][j] for j in xrange(L) if \
                wordList[i][j] in pattern[j]]
            if len(results) == L:
                result += 1
        print "Case #%d: %d" % (case, result)
        


if __name__ == '__main__':
    main()
