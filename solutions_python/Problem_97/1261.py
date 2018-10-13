

def getPairs(ints,A,B):
    first = 0
    last = len(ints)-1
    if(B < A):
        (A,B) = (B,A)
    ints.sort()
    while(first <= last and ints[first] < A):
        first+=1
    while(last >= first and ints[last] > B):
        last -= 1
    total = last-first+1
    return (total*(total-1))/2

max = 10000
gotten = [False for i in xrange(max)]

families = []
for r in xrange(1,max):
    if(not gotten[r]):
        gotten[r] = True
        x = str(r)
        p = [r]
        while(True):            
            x = x[1:] + x[0]
            if(x[0] != '0'):
                X = int(x)
                if(X <= max and not gotten[X]):
                    p.append(X)
                    gotten[X] = True
                else:
                    break
        families.append(p)
            


infile = open("C-small-attempt0.in","r")
outfile = open("C-small.out","w")

T = int(infile.readline())

for test in xrange(1,T+1):
    [A,B] = [int(token) for token in infile.readline().split()]
    answer = 0
    for f in families:
        answer += getPairs(f,A,B)
    outfile.write("Case #" + str(test) + ": " + str(answer) + "\n")
infile.close()
outfile.close()
