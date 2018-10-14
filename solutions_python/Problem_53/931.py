

#author:Rafael Pinheiro
import sys

#states
OFF = False
ON = True

class Snapper (object):
    '''
    Snapper object
    '''
    
    def __init__(self, plugged=False, state=OFF):
        '''
        init with plugged and state values
        '''
        self.state = state
        self.plugged = plugged
    
    def snap(self):
        '''
        called when a snap happen
        '''
        if self.plugged:
            self.state = not self.state

input_file = open(sys.argv[1])  

#number of snappers
n = None
#number of snaps
k = None
#num of test cases
t = None
#snappers line
snappers = None

lines = input_file.readlines()
t = int(lines[0])
for tc in range(1, t+1):
    n, k = lines[tc].split(' ')
    n = int(n)
    k = int(k)
    snappers = [Snapper() for x in range(n)]
    current = snappers[0]   
    current.plugged = True
    for snap in range(k):
        for s in range(n):
            current = snappers[s]
            current.snap()
        for s in range(n):
            previous = snappers[s-1] if s > 0 else None
            current = snappers[s]
            if previous and previous.plugged and previous.state:
                current.plugged = True
            elif previous and (not previous.plugged or not previous.state):
                current.plugged = False
            
    print('Case #%d: %s' % (tc, 'ON' if current.state and current.plugged else 'OFF'))
