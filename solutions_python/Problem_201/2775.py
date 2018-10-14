"""
Generates a bathroom with N+2 stalls, and the end occupied by 'guards'.
"""
import time
import random

class Bathroom:

    bathroom = []

    def __init__(self, N):
        bathroom = ['.']*(N+2)

        bathroom[0] = 'O'
        bathroom[-1] = 'O'

        self.bathroom = bathroom

    def calculateEmptyValues(self):
        emptyStalls = []

        for i in range( len( self.bathroom ) ):
            #bathroom is empty
            if self.bathroom[i] == '.':
                lcount, rcount = (0, 0)
                #find L_s
                for j in range(i-1, 0, -1):
                    if self.bathroom[j] == 'O':
                        break
                    lcount += 1

                #find R_s
                for j in range( i+1, len( self.bathroom ) ):
                    if self.bathroom[j] == 'O':
                        break
                    rcount += 1
                emptyStalls.append( ( i, ( lcount, rcount ) ) )

        return emptyStalls

    def maximiseEmptyStalls(self):
        stalls = self.calculateEmptyValues()

        minLR = lambda t: (t[0], min( t[1][0], t[1][1] ))
        maxLR = lambda t: (t[0], max( t[1][0], t[1][1] ))

        #find maximal min(Ls, Rs)
        mins = list( map( minLR, stalls ) )
        maxSpace = max( map( lambda l: l[1], mins ) )

        #filter list where they have this max
        stalls = list( filter( lambda t: min(t[1]) == maxSpace, stalls ) )

        #if there's only one stall with this max
        if len(stalls) == 1:
            return stalls[0][0]
        else:
            #else choose among those where max(Ls, Rs) is maximal
            maxs = list( map( maxLR, stalls ) )
            maxSpace = max( map( lambda l: l[1], maxs ) )

            stalls = list( filter( lambda t: t[1] == maxSpace, maxs ) )

            #automatically picks leftmost OR picks singleton element
            return stalls[0][0]

    def fillBathroom(self, K):
        #put K - 1 people into stals
        for _ in range( K - 1 ):
            i = self.maximiseEmptyStalls()

            assert self.bathroom[i] == '.'
            self.bathroom[i] = 'O'

        #find the max(Ls, Rs) and min(Ls, Rs) values
        emptyStalls = self.calculateEmptyValues()
        i = self.maximiseEmptyStalls()
        #mark the last person entered
        self.bathroom[i] = 'O'

        tup = [x[1] for x in emptyStalls if x[0] == i][0]

        return ( max(tup), min(tup) )

def main():
    testCases = int( input() )

    for test in range(1, testCases + 1):
        N, K = [int(s) for s in input().split(" ")]
        b = Bathroom(N)
        y, z = b.fillBathroom(K)
        print( "Case #" + str(test) + ":", y, z )

if __name__ == '__main__':
    main()
