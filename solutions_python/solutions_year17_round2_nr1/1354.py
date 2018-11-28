import math
def output (distance, arr):
    timearray = []
    minimum = 0
    index = 0
    for i in range (0, len(arr)):
        #print (arr[i][0])
        #print (arr[i][1])
        amountoftime = time(distance-arr[i][0], arr[i][1])
        #print (amountoftime)
        timearray.append (amountoftime)
        if i == 0 or amountoftime > minimum:
            #print ("Passing")
            minimum = amountoftime
            index = i

    return velocity (distance, minimum)

    


def velocity (d, t):
    return d/t

def time (d, v):
    return d/v

#def intersectionTime (
    
def getInput ():
    array = []
    with open('A-large.in.txt') as f:
        l = int (next(f))
        i = 1
        for lee in range (0, l): # read rest of lines
            array = [int(x) for x in next(f).split()]
            array2 = []
            for b in range (0, array[1]):
                array2.append ([int(x) for x in next(f).split()])
            out = output (array[0], array2)
            print ("Case #" +str(i) + ": %.6f"%out)

            i+=1

getInput()
