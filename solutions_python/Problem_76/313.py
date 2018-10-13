import os
import sys

def get_BinaryStr( value, digit = 0 ):
    rep = bin( value )[ 2 : ]
    return '0' * ( digit - len( rep ) ) + rep if digit > 0 else rep

def get_BinarySum( valueList, digit ):
    binarySum = '0' * digit

    for i in range( len( valueList ) ):
        rep = get_BinaryStr( valueList[ i ], digit )

        newBinarySum = ''
        
        for j in range( digit ):
            if binarySum[ j ] == rep[ j ]:
                newBinarySum += '0'
            else:
                newBinarySum += '1'

        binarySum = newBinarySum

    return binarySum
    
def main():
    totalCaseCount = int( sys.stdin.readline().strip( '\r\n' ) )

    for index in range( totalCaseCount ):
        valueCount = int( sys.stdin.readline().strip( '\r\n' ) )
        valueList = sorted( [ int( value ) for value in sys.stdin.readline().strip( '\r\n' ).split() ] )

        maxValue = valueList[ -1 ]
        maxValueDigit = len( get_BinaryStr( maxValue ) )

        for i in range( len( valueList ) ):
            if get_BinarySum( valueList[ : i + 1 ], maxValueDigit ) == get_BinarySum( valueList[ i + 1 : ], maxValueDigit ):
                print( 'Case #{}: {}'.format( index + 1, sum( valueList[ i + 1 : ] ) ) )
                break
        else:
            print( 'Case #{}: NO'.format( index + 1 ) )

if __name__ == '__main__':
    main()
