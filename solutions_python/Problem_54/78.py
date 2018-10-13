def gcd(a,b):
    while (b != 0):
        c = a%b
        a = b
        b = c
    return a

def get_gcd(line):
    g = line[0]
    cnt = len(line)
    for i in range(1,cnt):
        g = gcd(g,line[i])
    return g

def solve(line):
    N = int(line.pop(0))
    for i in range(0,N):
        line[i] = int(line[i])
    line.sort()
    diffs = list()
    for i in range(0,N-1):
        diff = line[i+1] - line[i]
        diffs.append(diff)
    g = pg = get_gcd(diffs)
    if g < line[0]:
        g = line[0] / pg * pg
        if line[0] % pg != 0:
            g += pg
    ans = g - line[0]
    return ans

AnsT = ""
myfile = open("B.in")
T = int(myfile.readline())
for i in range(0,T):
    line = myfile.readline()
    line = line.split("\n")
    print i
    ans = solve(line[0].split(" "))
    AnsT = AnsT + "Case #"+ str(i+1) +": "+str(ans) + "\n"

outfile = open("B.out","w")
outfile.write(AnsT)
outfile.close()
