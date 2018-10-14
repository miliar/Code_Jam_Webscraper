## code jam qualification round 2008
## saving the universe

infty = 1e10

def find(x, L):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return infty

inputf = open('A-large.in','r')
outputf = open('A-large.out','w')

inputL = inputf.readlines()
for i in range(len(inputL)):
    inputL[i] = inputL[i].rstrip()
N = int(inputL[0])
cases = []
start_line = 1
for i in range(1,N+1):
    cases.append([[],[]]) # for each case init 2 lists for search engines & queries
    end_line = start_line + int(inputL[start_line]) + 1
    cases[i-1][0] = inputL[start_line+1:end_line]
    start_line = end_line
    end_line = start_line + int(inputL[start_line]) + 1
    cases[i-1][1] = inputL[start_line+1:end_line]
    start_line = end_line

## done parsing input, now compute for each case

for i in range(1,N+1):
    [engines, queries] = cases[i-1]
    switches = {} # switches[(e,q)] = #switches needed if at query q and engine e
    q = len(queries)
    for e in engines:
        switches[(e,q)] = 0
    q -= 1
    while q >= 0:
        for e in engines:
            if e == queries[q]:
                switches[(e,q)] = infty
            else:
                same = switches[(e,q+1)]
                diff = 1 + min([switches[(e_next,q+1)] for e_next in engines])
                switches[(e,q)] = min([same, diff])
        q -= 1
    outputf.write('Case #%d: %d\n' % (i, min([switches[(e,0)] for e in engines])))

inputf.close()
outputf.close()
