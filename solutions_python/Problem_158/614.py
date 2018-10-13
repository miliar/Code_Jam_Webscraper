def readint(input):
    return int(input.readline().strip('\n'))

def readstr(input):
    return input.readline().strip('\n')


def readintline(intput):
    return [int(i) for i in input.readline().strip('\n').split(' ')]

def readstrline(intput):
    return [i for i in input.readline().strip('\n').split(' ')]
  
def solve(X,R,C):
    if (R * C) % X == 0 and R > (X - 2) and C > (X - 2):
        return 'GABRIEL'
    else:
        return 'RICHARD'

with open('D-small-attempt0.in','r') as input:
    with open('D-small-attempt0.out','w') as output:
        cases = readint(input)
        for case in xrange(1,cases+1):
            X,R,C = readintline(input)
            result = solve(X,R,C)
            output.write('Case #%s: %s\n' % (str(case),str(result)))

print 'Done'