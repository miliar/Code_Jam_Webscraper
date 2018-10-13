import psyco
wtcj = "welcome to code jam"

def try_one(s, i, wi):
    if i >= len(s) or s[i] != wtcj[wi]:
        return 0
    if wi+1 >= len(wtcj):
        return 1
    return sum((try_one(s, ni, wi+1) for ni in xrange(i+1, len(s))))
psyco.bind(try_one)
def main():
    n = int(raw_input())
    for i in xrange(n):
        line = raw_input()
        print "Case #%d: %04d" % ( i+1, sum((try_one(line, j, 0) for j in xrange(len(line)))) % 10000)

main()
