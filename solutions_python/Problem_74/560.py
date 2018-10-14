import sys


def main():
    with open( sys.argv[1] ) as f :
        content = map( lambda x: x.rstrip() , f.readlines())

    totalCount = int( content.pop(0) )
    result = map( processCase , content )
    for index , ret in enumerate(result):
        print "Case #%d: %d" % ( index + 1 , ret )


def processCase( case ):
    case = case.split(' ')
    stepsCount = case.pop(0)

    finalTime = 0
    passedTime = 0
    pos = { 'O' : 1 , 'B' : 1 , 'last' : None }
    while case :
        robot , button = case[0] , int( case[1] )
        case.pop(0)
        case.pop(0)

        if pos['last'] is None or pos['last'] == robot : # first time
            moveClickTime = abs( pos[robot] - button ) + 1
            passedTime += moveClickTime
            finalTime += moveClickTime
        else:
            moveTime = abs( pos[robot] - button )
            moveTime = 0 if passedTime >= moveTime else moveTime - passedTime

            passedTime = moveTime + 1
            finalTime += passedTime
        pos[robot] = button
        pos['last'] = robot

    return finalTime










if __name__ == '__main__':
    main()
