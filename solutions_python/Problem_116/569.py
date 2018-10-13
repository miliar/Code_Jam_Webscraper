
import sys

data = sys.stdin.readlines()

nbSamples = int(data.pop(0))
# print "nbSamples: ", nbSamples

def equal(x, y):
    return ((x == y) or (x == 2) or (y == 2)) and (x != 3) and (y != 3)

for sample in range(nbSamples):
    
    # Get the array
    arraystring = {}
    array = {}
    
    for li in range(4):
        arraystring[li] = data.pop(0).rstrip();

    # Transform in full int array
    for li in range(4):
        nbco = 0
        for co in arraystring[li]:
            if co == 'X':
                array[li, nbco] = 0
            elif co == 'O':
                array[li, nbco] = 1
            elif co == 'T':
                array[li, nbco] = 2
            elif co == '.':
                array[li, nbco] = 3
            nbco = nbco + 1

    # Get the answer
    print "Case #" + str(sample+1) + ":",

    # Test in lines
    stop = 0

    for li in range(4):
        check = 1
        for ii in range(4):
            for jj in range(4):
                if not equal(array[li, ii], array[li, jj]):
                    check = 0

        if check:
            if (array[li, 0] == 0) or (array[li, 1] == 0):
                print "X won"
            elif (array[li, 0] == 1) or (array[li, 1] == 1):
                print "O won"
            else:
                print "what A?", array[li, 0], " ", array[li, 1]
            stop = 1
            break

    if stop:
#        print "(lines)"
        data.pop(0);
        continue;

    li = 1000

    # Test in columns
    for co in range(4):
        check = 1
        for ii in range(4):
            for jj in range(4):
                if not equal(array[ii, co], array[jj, co]):
                    check = 0

        if check:
            if (array[0, co] == 0) or (array[1, co] == 0):
                print "X won"
            elif (array[0, co] == 1) or (array[1, co] == 1):
                print "O won"
            else:
                print "what B?"
            stop = 1
            break

    if stop:
#        print "(columns)"
        data.pop(0);
        continue;

    co = 1000

    # Test the cross A
    check = 1
    for ii in range(4):
        for jj in range(4):
            if not equal(array[ii, ii], array[jj, jj]):
                check = 0

    if check:
        if (array[0, 0] == 0) or (array[1, 1] == 0):
            print "X won"
        elif (array[0, 0] == 1) or (array[1, 1] == 1):
            print "O won"
        else:
            print "what B?"
        stop = 1

    if stop:
 #       print "(cross A)"
        data.pop(0);
        continue;

    # Test the cross B
    check = 1
    for ii in range(4):
        for jj in range(4):
            if not equal(array[ii, 3 - ii], array[jj, 3 - jj]):
                check = 0

    if check:
        if (array[0, 3 - 0] == 0) or (array[1, 3 - 1] == 0):
            print "X won"
        elif (array[0, 3 - 0] == 1) or (array[1, 3 - 1] == 1):
            print "O won"
        else:
            print "what B?"
        stop = 1

    if stop:
#        print "(cross B)"
        data.pop(0);
        continue;

    # Check if the array is full
    for li in range(4):
        for co in range(4):
            if array[li, co] == 3:
                print "Game has not completed"
                stop = 1
                break
        if stop:
            break

    if stop:
        data.pop(0);
        continue;

    print "Draw"
    data.pop(0);

