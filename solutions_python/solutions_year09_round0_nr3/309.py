# Mallin Moolman

w = "welcome to code jam"
valid = list(set(list(w)))

filename = "C-small-attempt0.in"
f = open (filename)
outfile = open (filename.rsplit(".", 1)[0] + ".out", 'w')

def findall (l, v):
    index = -1
    out = []
    while True:
        try:
            index = l.index(v, index+1)
            out.append(index)
        except ValueError:
            break

    return out

def oper (s, pos):
    if pos == len(w):
        return 1
    else:
        tot = 0
        for a in findall (s, w[pos]):
            tot += oper(s[a:], pos+1)
        return tot%10000
    
n = int(f.readline().strip())

for case in xrange(n):
    line = f.readline().strip()
    line = [char for char in line if char in valid]


            

    num = oper (line, 0)

    outfile.write( "Case #%d: %s" % (case+1, str(num).zfill(4)) + "\n")

f.close()
outfile.close()
