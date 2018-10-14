__author__ = 'faet'
import math




def checkit(first, second):
    count = 0
    squares = [1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004]
    for n in squares:
        if n in range(first, second+1):
            count += 1

    return count

ins = open( "sqr.txt" )
count = ins.readline()
game = ''

for j in range(int(count)):
    for i in range(1):
        game+=ins.readline()
        first = game[:game.find(' ')]
        second = game[game.find(' ')+1:]
        tot=checkit(int(first),int(second))
        print "Case #"+str(j+1)+": "+str(tot)
    game = ''
ins.close()