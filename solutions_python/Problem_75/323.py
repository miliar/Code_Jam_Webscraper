import os
import sys

def main():
    totalCaseCount = int( sys.stdin.readline().strip( '\r\n' ) )

    for index in range( totalCaseCount ):
        case = sys.stdin.readline().strip( '\r\n' ).split()
        caseIndex = 0

        combine = dict()
        opposed = list()

        combineCount = int( case[ caseIndex ] )
        caseIndex += 1

        for i in range( combineCount ):
            combineElem = case[ caseIndex ]
            caseIndex += 1

            combine[ ( combineElem[ 0 ], combineElem[ 1 ] ) ] = combineElem[ 2 ]
            combine[ ( combineElem[ 1 ], combineElem[ 0 ] ) ] = combineElem[ 2 ]

        opposedCount = int( case[ caseIndex ] )
        caseIndex += 1

        for i in range( opposedCount ):
            opposedElem = case[ caseIndex ]
            caseIndex += 1
            
            opposed.append( ( opposedElem[ 0 ], opposedElem[ 1 ] ) )
            opposed.append( ( opposedElem[ 1 ], opposedElem[ 0 ] ) )

        elemCount = int( case[ caseIndex ] )
        elemList = case[ caseIndex + 1 ]

        outputList = list()

        for elem in elemList:
            outputList.append( elem )

            while len( outputList ) >= 2:
                key = ( outputList[ -1 ], outputList[ -2 ] )
                
                if key in combine:
                    outputList.pop()
                    outputList.pop()                
                    outputList.append( combine[ key ] )
                    continue

                for i in range( len( outputList ) ):
                    key = ( outputList[ i ], outputList[ -1 ] )

                    if key in opposed:
                        outputList = list()
                        break

                break
                
        print( 'Case #{}: ['.format( index + 1 ), end = '' )
        for i, elem in enumerate( outputList ):
            print( elem, end = '' )
            if i < len( outputList ) - 1:
                print( ', ', end = '' )

        print( ']' )

if __name__ == '__main__':
    main()
