inputF = open('A-large.in', 'r')
output = open('A-large.out', 'w')

numCases = int(inputF.readline())

def getMaxSpeed(d, horses):
    ''' Horses is a list of (speed, location) tuples '''
    latestArrival = 0
    for (speed, loc) in horses:
        t = (d-loc)*1.0/speed
        #print speed, loc, d, t
        if t > latestArrival:
            latestArrival = t
    return d/latestArrival

for i in range(numCases):
    d, n = inputF.readline().split()
    horses = []
    for j in range(int(n)):
        line = inputF.readline().strip().split()
        horses += [(int(line[1]), int(line[0]))]
    speed = getMaxSpeed(int(d), horses)

    output.write('Case #' + str(i+1) + ': ' + str(speed) + '\n')
inputF.close()
output.close()
