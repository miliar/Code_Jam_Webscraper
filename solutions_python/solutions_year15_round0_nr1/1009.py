def readint(input):
    return int(input.readline().strip('\n'))

def readintline(intput):
    return [int(i) for i in input.readline().strip('\n').split(' ')]

def readstrline(intput):
    return [i for i in input.readline().strip('\n').split(' ')]
    
    
def solve(smax,aud):
    result = 0
    
    cul = 0
    for i in xrange(1,smax+1):
        cul += aud[i-1]
        if aud[i] > 0 and i > cul:
            #invite friends
            friends = i - cul
            aud[i] += friends
            result += friends
    
    return result

with open('A-large.in','r') as input:
    with open('A-large.out','w') as output:
        cases = readint(input)
        for case in xrange(1,cases+1):
            values = readstrline(input)
            smax = int(values[0])
            aud = [int(i) for i in values[1]]
            result = solve(smax,aud)
            output.write('Case #%s: %s\n' % (str(case),str(result)))

print 'Done'