import numpy
import re
import copy

# Function to reduce the given problem to lowest equivalent problem
def reduceProblem(numStalls, numPeople):
    reducedNumStalls = numStalls
    reducedNumPeople = numPeople
    while True:
        if reducedNumStalls == reducedNumPeople:
            reducedNumStalls = 0
            reducedNumPeople = 0
            break
        if reducedNumPeople == 1:
            break
        # Reduce to half of the numbers
        if reducedNumStalls % 2 == 0 \
            and reducedNumPeople % 2 == 1:
            # if num stalls is even, and num people is odd,
            # then the reduced num stalls is 1 less than half of num stalls
            reducedNumPeople = int(reducedNumPeople / 2)
            reducedNumStalls = int(reducedNumStalls / 2)
            reducedNumStalls -= 1
        else:
            reducedNumPeople = int(reducedNumPeople / 2)
            reducedNumStalls = int(reducedNumStalls / 2)

    return (reducedNumStalls, reducedNumPeople)

t = int(input()) # Number of test cases
for i in range(t):
    s = input() # Given test case string
    (numStalls, numPeople) = (int(x) for x in s.split(' '))
    (reducedNumStalls, reducedNumPeople) = reduceProblem(numStalls, numPeople)
    (maxNumEmptyStalls, minNumEmptyStalls) = (reducedNumStalls, reducedNumPeople)
    if maxNumEmptyStalls != 0:
        maxNumEmptyStalls = int(maxNumEmptyStalls/2)
        minNumEmptyStalls = maxNumEmptyStalls
        if reducedNumStalls % 2 == 0:
            minNumEmptyStalls -= 1
    print("Case #{}: {} {}".format(i + 1, maxNumEmptyStalls, minNumEmptyStalls))
