import sys

def main():
    with open( sys.argv[1] ) as f:
        content = map( lambda x : x.rstrip() , f.readlines() )

    totalCount = content.pop(0)

    result = map( processCase , content )

    for index , ret in enumerate( result ):
        print "Case #%d: [%s]" % ( index + 1 , ", ".join( ret ) )


def processCase( case ):
    case = case.split(' ')
    composeDict = {}
    composeCount = int( case.pop(0) )
    while composeCount :
        recipe = case.pop(0)
        composeDict[ recipe[1] + recipe[0] ] = recipe[2]
        composeDict[ recipe[0] + recipe[1] ] = recipe[2]
        composeCount -= 1

    oppositeList = []
    oppositeCount = int( case.pop(0) )
    while oppositeCount:
        opposite = case.pop(0)
        oppositeList.append( set( [ opposite[0] , opposite[1] ] ) )
        oppositeCount -= 1

    baseLength = int( case.pop(0) )
    baseList = list( case.pop(0) )
    finalList = []
    while baseList:
        finalList.append( baseList.pop(0) )

        if len( finalList ) == 1:
            continue

        key = finalList[-2] + finalList[-1]
        if key in composeDict:
            finalList = finalList[:-2] + [ composeDict[key] ]
            continue

        for x in oppositeList:
            if x.issubset( finalList ):
                finalList = []
                break

    return finalList




if __name__ == '__main__':
    main()
