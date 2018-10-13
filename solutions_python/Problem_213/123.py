# I run this with python 3.4.3

import numpy as np # used for arrays e.g.; Can be downloaded from www.numpy.org

# I use filenames for input/output
debug=False
#filename = 'sample.in'
filename = 'B-small-attempt0.in'
outputFilename = filename.replace('in','out')

def runAlgorithm( seatCount, customerCount, ticketCount, tickets ):
    customers = [[] for _ in range( customerCount ) ] # contains lists of the seats ordered by each customer
    for t in tickets:
        customers[ t[1]-1 ].append( t[0]-1 )
    customerLengths = [len(c) for c in customers]
    indices = np.argsort(customerLengths)[::-1]
    customersSorted = []
    for i in indices:
        customersSorted.append( customers[i] )
##    print( customersSorted )
    rideCount = max( customerLengths )
    rideCount = max( rideCount, ticketCount // seatCount )
    print( 'start with', rideCount, 'rides' )
    while True:
        rollercoaster = np.zeros( shape=(rideCount, seatCount) )
        promotionCount = 0
        gotoNextRide = False
        for customer in customersSorted:
##            print('new Customer')
            for desiredSeat in customer:
                gotoNextTicket = False
##                print('new Ticket')
                for seatIndex in list(range(desiredSeat+1))[::-1]:
##                    print( 'list(range(desiredSeat+1))[::-1]', list(range(desiredSeat+1))[::-1] )
                    for rideIndex in range(len(rollercoaster)):
##                        print( 'ride {} seat {}'.format( rideIndex, seatIndex ) )
                        if rollercoaster[rideIndex][seatIndex] == 0:
                           rollercoaster[rideIndex][seatIndex] = 1 # occupy
                           if seatIndex != desiredSeat:
                               promotionCount += 1
                           gotoNextTicket = True
##                           print( 'customer', customer )
##                           print( 'got seat {} in ride {}'.format( seatIndex, rideIndex ) )
                           break
                    if gotoNextTicket:
                        break
                if not gotoNextTicket:
                    print( 'no solution for rideCount = ', rideCount )
##                    print( rollercoaster )
                    rideCount += 1
                    gotoNextRide = True
                    break
            if gotoNextRide:
                break
        return rideCount, promotionCount
        

# handle file input/output and call above algorithm for each case
open( outputFilename, 'w' ) # clear output file
with open(filename, 'r') as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print('i:', i) # show progress
        data = f.readline().strip().split(' ')
        seatCount = int( data[0] )
        customerCount = int( data[1] )
        ticketCount = int( data[2] )
        tickets = [] # (position, customer)
        for m in range( ticketCount ):
            data = f.readline().strip().split(' ')
            position = int( data[0] )
            customer = int( data[1] )
            tickets.append( [position, customer] )
        result = runAlgorithm( seatCount, customerCount, ticketCount, tickets )
        with open( outputFilename, 'a' ) as f2:
            outputLine = 'Case #{}: '.format(i) + '{} {}'.format( result[0], result[1] )
            if debug:
                print(outputLine)
            f2.write( outputLine + '\n')
            
