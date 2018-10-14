#!/usr/bin/python
import numpy as np
import math

def recurse(nodes, counter, people, result):

    length = len(nodes)
    newnodes = []
    for x in range(0, length):        
        counter = counter+1
        
        left  = math.floor( (nodes[x]-1)/2 )
        right = math.ceil( (nodes[x]-1)/2 )
        newnodes.append(right)
        newnodes.append(left)
        
        if(counter == people ):
            result.append(left)
            result.append(right)
            result.sort(reverse=True)
            return result
        
    newnodes.sort(reverse=True)
    recurse(newnodes, counter, people, result)

#-----------------------------------------------------

def bestBathrooms(baths, people, output):

    print("Number of bathrooms and people ", baths, " ", people)

    # Find nearest power of 2 that is smaller than the
    # number of bathrooms

    # Also find the largest power of true smaller than the
    # number of people

    power = 0
    powerpeople = 0
    while(2**power <= baths/2):
        power = power + 1
    while(2**powerpeople <= people/2):
        powerpeople = powerpeople + 1

    print("power, exp ", power, 2**power)
    print("powerpeople, exp ", powerpeople, 2**powerpeople)

    nodes = [baths]
    recurse(nodes, 0, people, output)
    print('ret ', output)
    return 

#-----------------------------------------------------
    
fin = open("bath_sample.txt", "r")
number_of_test_cases = int(fin.readline()) ;
print("Number of test cases: ", number_of_test_cases)

fout = open('bath_output.txt', 'w')

for x in range(0, number_of_test_cases):
    string  = fin.readline()

    parts   = string.split()
    baths   = int(parts[0])
    people  = int(parts[1])

    output =  []
    bestBathrooms(baths, people, output)
    
    output_string = 'Case #' + str(x+1) + ": " + str(output[0]) + " " + str(output[1]) + "\n" 

    print(output_string)
    fout.write(output_string)
    
fout.close()
fin.close()
