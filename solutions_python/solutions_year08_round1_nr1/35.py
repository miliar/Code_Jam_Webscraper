## google code jam 2008, round 1a
## minimum scalar product

inputf = open('A-large.in','r')
outputf = open('A-large.out','w')
lines = inputf.readlines()
N = int(lines[0])

def dot_prod(v1,v2):
    sum = 0
    for i in range(len(v1)):
        sum += v1[i]*v2[i]
    return sum

for case in range(1,N+1):
    n = int(lines[case*3-2])
    v1 = map(int, lines[case*3-1].split())
    v2 = map(int, lines[case*3].split())
    v1.sort()
    v2.sort()
    v2.reverse()
    outputf.write('Case #%d: %d\n' % (case,dot_prod(v1,v2)))

inputf.close()
outputf.close()
