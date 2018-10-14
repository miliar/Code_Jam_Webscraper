import sys

def is_tidy(n):
    n = str(n)
    for i in xrange(len(n)-1):
        if ord(n[i]) > ord(n[i+1]):
            return False
    return True

def solve(path):
    L = open(path, "rb").read().splitlines()[1:]
    t = 1
    for line in L:
        line.strip()
        print "Case #%d:" % t,
        t += 1

        if is_tidy(line):
            res = line
            found = True
        else:
            for b in xrange(len(line)-1, -1, -1):
                if line[b] == '0':
                    continue
                if (b == 0) and (line[b] == '1'):
                    res = "9"*(len(line)-1)
                    found = True
                    break
                res = line[:b] + chr(ord(line[b])-1)
                res += "9"*(len(line)-len(res))
                if is_tidy(res):                
                    found = True
                    break
            
        #for i in xrange(int(res)+1, int(line)+1):
        #    if is_tidy(i):
        #        print "WRONG! %d %s %s" % (i, res, line)
        assert is_tidy(int(res)), "WRONG: %s %s" % (res, line)
        print res

if __name__ == "__main__":
    solve(*sys.argv[1:])
            
