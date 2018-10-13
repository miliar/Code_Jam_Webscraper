
targetStr = "welcome to code jam"

def countSubstr(s, p):
    rows = len(p)
    cols = len(s) + 1
    countM = [[1]*cols] + [[0]*cols for i in range(rows)]
    for i in range(1, rows+1):
        for j in range(1, cols):
            if s[j-1] == p[i-1]:
                countM[i][j] = (countM[i-1][j-1] + countM[i][j-1])%100000
            else:
                countM[i][j] = countM[i][j-1]
    return countM[rows][cols-1]
def main(f):
    fo = open(f, 'r')
    T = int(fo.readline())
    for i in range(T):
        print "Case #%d: %04d" % (i+1, countSubstr(fo.readline(), targetStr))
    fo.close()

if __name__=='__main__':
    import sys
    main(sys.argv[1])
