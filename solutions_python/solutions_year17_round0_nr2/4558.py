import math

TESTING = False
PROB_NAME = 'B'
IN_FILE = 'tiny.in' if TESTING else ("%s.in" % (PROB_NAME  ,))
OUT_FILE = "%s.out" % (PROB_NAME,)

in_f = open(IN_FILE)
out_f = None if TESTING else open(OUT_FILE, 'w')

lines =in_f.readlines()

def prntSol(cs_n, ln):
    to_p = "Case #%s: %s" % (cs_n, str(ln).lstrip().rstrip())
    if TESTING:
        print(to_p)
    else:
        out_f.write("%s\n" % (to_p))

def isSorted(s):
    return ''.join(s) == ''.join(sorted(s))

def solveIt(ln):
    if isSorted(ln) == 1:
        return ln
    ln = list(ln)
    for i in range(1, len(ln)):
        if(isSorted(ln[:-i])):
            suffix = ''.join(['9']*(len(ln) - len(ln[:-i])))

            pr = ''.join(list(map(lambda x : x, ln[:-i])))
            pp_r = str(int(pr) - 1)
            
#            print('suffix -> %s, prefix -> %s', (suffix,solveIt(pr)))

            return solveIt(pp_r) + suffix
#            return int("%s%s" % (''.join(list(map(lambda x : str(x), pr))), suffix))

    

for i, line in enumerate(lines[1:]):
    prntSol(i + 1, int(solveIt(line.lstrip().rstrip())))
    
if not TESTING: out_f.close()
in_f.close()
