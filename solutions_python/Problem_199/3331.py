from functools import reduce;
import sys

def is_well_done(row):
    return reduce(lambda x,y : x and y,row)

def still_work(row,flipper,index):
    size = len(row)
    return index+flipper <= size

f =  open('A-small-attempt1.in', 'r')

N = f.readline()
N = int(N)

for case in range(N):
    data_in = f.readline()
    pancakes, flipper = data_in.split()

    flipper = int(flipper)
    pancakes = [charac == '+' for charac in pancakes]

    index = 0
    counter = 0

    while index < len(pancakes) and pancakes[index] :
        index += 1

    while is_well_done(pancakes) == False and still_work(pancakes,flipper,index):
        for i in range(flipper):
            pancakes[i + index] = not pancakes[i + index]

        while index < len(pancakes) and pancakes[index] :
            index += 1

        counter +=1

    case += 1

    output =  "Case #%i:" % (case )

    if is_well_done(pancakes):
        output += " %i" % (counter)
    else:
        output += " IMPOSSIBLE"

    print (output)
