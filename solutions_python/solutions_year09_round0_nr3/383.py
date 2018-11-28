import sys

sys.setrecursionlimit(10000)

fin = file("C-large.in", "r")
fout = file("C-large.out", "w")

N = int(fin.readline())
string = "welcome to code jam"

def r(cs, ss):
    """case start; string start"""
    if ss == 18:
        return case[cs:].count("m")
    if cs >= l:
        return 0
    if memo.has_key((cs+1, ss)):
        a = memo[(cs+1, ss)]
    else:
        a = r(cs+1, ss)
        memo[(cs+1, ss)] = a
    #a = r(cs+1, ss)
    if case[cs] == string[ss]:
        return r(cs+1, ss+1) + a
    return a

for caseno in xrange(N):
    memo = {}
    case = fin.readline().rstrip()
    l = len(case)
    #print case, l
    answer = r(0, 0)
    #print answer
    fout.write("Case #%i: %.4i\n" % (caseno + 1, answer % 10000))

fin.close()
fout.close()
