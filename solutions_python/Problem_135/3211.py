
import sys
import traceback

def readTestCase():
    test = {}
    test['first'] = dict( row = int(sys.stdin.readline().strip()) )
    test['first']['cards'] = [ [ int(n) for n in sys.stdin.readline().strip().split(' ') ] for i in range(4) ]
    test['second'] = dict( row = int(sys.stdin.readline().strip()) )
    test['second']['cards'] = [ [ int(n) for n in sys.stdin.readline().strip().split(' ') ] for i in range(4) ]
    return test

def testCase( num, test ):
    cards = ( set(test['first']['cards'][ test['first']['row'] - 1 ])
            & set(test['second']['cards'][ test['second']['row'] - 1 ]) )

    if len(cards) == 1:
        output = str(cards.pop())
    elif len(cards) > 1:
        output = "Bad magician!"
    else:
        output = "Volunteer cheated!"

    print "Case #%i: %s" % ( num, output )

def main():
    total = int(sys.stdin.readline().strip())
    num = 1
    while num <= total:
        testCase( num, readTestCase() )
        num += 1

main()
