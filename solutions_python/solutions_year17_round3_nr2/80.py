# I run this with python 3.6.1

import numpy as np # used for arrays e.g.; Can be downloaded from www.numpy.org

# I use filenames for input/output
debug=False
#filename = 'sample.in'
#filename = 'B-small-attempt0.in'
filename = 'B-large.in'
outputFilename = filename.replace('in','out')

class Activity:
    def __init__(self, C, D, person):
        self.start = C
        self.end = D
        self.person = person
    def __lt__(self, other):
         return self.start < other.start
    def __str__(self):
        return 'Activity( "{}", {}, {} )'.format( self.person, self.start, self.end )
    __repr__ = __str__

def inversePerson( person ):
    if person == 'C':
        return 'J'
    elif person == 'J':
        return 'C'
    else:
        raise ValueError( person )

def runAlgorithm( AC, AJ, activities ):
    activities = sorted( activities )
    time = {'C': 720, 'J': 720}
    for a in activities:
        assert a.person in ['C', 'J']
        time[a.person] -= (a.end-a.start)
    hasMidnightJump = 0
    while True:
        if debug:
            print( len(activities) )
            print( activities )
        joinCandidate = None
        insertActivity = None
        for i in range(len(activities)-1):
            if activities[i].person != activities[i+1].person:
                continue
            distance = activities[i+1].start - activities[i].end
            if time[ activities[i].person ] < distance:
                insertActivity = [ i+1, Activity(activities[i].end, activities[i].end+1, inversePerson(activities[i].person)) ]
                break
            if joinCandidate is None:
                joinCandidate = [distance, i]
            elif joinCandidate[0] > distance:
                joinCandidate = [distance, i]
        # last activity is different -> midnight
        if activities[0].person == activities[len(activities)-1].person:
            distance = activities[0].start + 2*720 - activities[len(activities)-1].end
            if distance != 0:
                if time[ activities[0].person ] >= distance:
                    if joinCandidate is None:
                        joinCandidate = [distance, len(activities)-1]
                    elif joinCandidate[0] > distance:
                        joinCandidate = [distance, len(activities)-1]
                else:
                    if activities[len(activities)-1].end == 2*720:
                        insertActivity = [ len(activities), Activity(0, 1, inversePerson(activities[0].person)) ]
                    else:
                        insertActivity = [ len(activities), Activity(activities[len(activities)-1].end, activities[len(activities)-1].end+1, inversePerson(activities[0].person)) ]
            else:
                hasMidnightJump = 1
        if not insertActivity is None:
            activities.insert( insertActivity[0], insertActivity[1] )
            continue
        if joinCandidate is None:
            break
        person = activities[joinCandidate[1]].person
        if joinCandidate[1] == len(activities)-1:
            activities[0].start = 0
            activities[len(activities)-1].end = 2*720
            time[person] -= joinCandidate[0]
        else:
            time[person] -= joinCandidate[0]
            activities[ joinCandidate[1] ].end = activities[ joinCandidate[1]+1 ].end
            activities.pop( joinCandidate[1]+1 )        
    return len(activities) - hasMidnightJump

# handle file input/output and call above algorithm for each case
open( outputFilename, 'w' ) # clear output file
with open(filename, 'r') as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print('i:', i) # show progress
        data = f.readline().strip().split(' ')
        AC = int( data[0] )
        AJ = int( data[1] )
        activities = []
        for a in range(AC):
            data = f.readline().strip().split(' ')
            C = ( int( data[0] ) )
            D = ( int( data[1] ) )
            activities.append( Activity(C, D, 'C') )
        for a in range(AJ):
            data = f.readline().strip().split(' ')
            C = ( int( data[0] ) )
            D = ( int( data[1] ) )
            activities.append( Activity(C, D, 'J') )
        result = runAlgorithm( AC, AJ, activities )
        with open( outputFilename, 'a' ) as f2:
            outputLine = 'Case #{}: '.format(i) + '{}'.format(result)
            if debug:
                print(outputLine)
            f2.write( outputLine + '\n')
            
