import sys, string

def roll(s, amt):
    return s[amt:] + s[:amt]

def numPairs(A, B):
    pairs = 0
    for n in range(A, B):
        for m in range(n + 1, B+1):
            nStr = string.zfill(str(n), len(str(A)))
            mStr = string.zfill(str(m), len(str(A)))
            for i in range(len(nStr)):
                if mStr==roll(nStr, i):
                    #print mStr, nStr
                    pairs += 1
    return pairs

if __name__=='__main__':
    infile = open(sys.argv[1])
    lines = []
    output = []
    infile.readline()
    for line in infile:
        lines.append(line.rstrip())
    caseNum = 1
    for line in lines:
        a, b = line.split()
        output.append("Case #" + str(caseNum) + ": " + 
                      str(numPairs(int(a), int(b))))
        caseNum += 1
    out = open('out.out', 'w')
    for line in output:
        out.write(line + '\n')
