import string

def concat(file):
    input = []
    for l in open(file, "r"):
        input.extend("".join(l.strip().split(' ')))
    return input

if __name__ == "__main__":
    inp = concat("A.din")
    outp = concat("A.dout")
    d = {}
    for i in range(len(inp)):
        d[inp[i]] = outp[i]
    d['z'] = 'q'
    d['q'] = 'z'
    
    
    fin = open("A.in", "r")
    fout = open("A.out", "w")
    
    n = int(fin.readline())
    
    for cas in range(n):
        l = "".join((d.get(v, v) for v in fin.readline().strip()))
        print  >> fout, ("Case #%d: %s" % (cas + 1, l))
