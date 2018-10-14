import os
import re

def line(f):
    return f.readline().replace("\n","")
def items_line(f, split=" "):
    return line(f).split(split)
def items_line_limit(f, limit, split=" "):
    return line(f).split(split, limit)
def int_line(f):
    return int(line(f))
def ints_line(f, split=" ", limit=None):
    line = items_line_limit(f, limit, split=split) if limit else items_line(f, split=split)
    return map(int, line)


def run(infile, outfile):
    f = open(infile)
    out = open(outfile,"w")
    L, D, N = ints_line(f)
    words = []
    for d in range(D):
        words.append(line(f))
    for n in range(N):
        case_arr = re.split("(\([^\(]*\))", line(f))
        case = [c for c in case_arr if c]
        case = [(lambda c: list(c) if not c.startswith("(") and not c.endswith(")") else c)(c) for c in case]
        ncase = []
        for c in case:
            if isinstance(c, list):
                ncase+=c
            else:
                ncase.append(c)
        ncase=[list(re.sub("[()]","",c)) for c in ncase]
        count = 0
        for word in words:
            ok = True
            for i, w in enumerate(word):
                if w not in ncase[i]:
                    ok = False
                    break
            if ok:
                count += 1
        print n
        out.write("Case #%d: %d\n" % (n+1, count))
    
    out.close()
    f.close()

def check(outfile, answer):
    out = open(outfile)
    ans = open(answer)
    assert out.read() == ans.read()
    ans.close()
    out.close()
    print "ok"

if __name__=="__main__":
    name = os.path.splitext(os.path.basename(__file__))[0]
    run("inputs/%s.in" % name, "outputs/%s.out" % name)
    #check("outputs/%s.out" % name, "outputs/%s.ans" % name)
