import sys
import itertools
import operator


def main():
    with open( sys.argv[1] ) as f:
        content = map( lambda x : x.rstrip() , f.readlines() )



    totalCase = content.pop(0)
    content = content[1::2]

    result = map( processCase , content )
    for index , ret in enumerate( result ):
        print "Case #%d: %s" % ( index + 1 , "NO" if ret == 0 else "%d" % ret )

def processCase( case ):
    case = map( int , case.split(" "))
    case.sort()

    maxValue = 0
    
    for leftPileCount in range( 1 , len( case ) /2 + 1 ):
        for leftPile in itertools.combinations( case , leftPileCount ):
            rightPile = getAnotherPile( case , leftPile )
            if PatrickAdd( leftPile ) == PatrickAdd( rightPile ):
                maxValue = max( SeanAdd( leftPile ) , SeanAdd( rightPile ) , maxValue )

    return maxValue


def PatrickAdd( items ):
    return reduce( operator.xor ,  items )

def getAnotherPile( allPile , onePile ):
    anotherPile = allPile[:]
    for x in onePile:
        anotherPile.remove( x )
    return anotherPile



def SeanAdd( items ):
    return reduce( operator.add  , items )






if __name__ == '__main__':
    main()
