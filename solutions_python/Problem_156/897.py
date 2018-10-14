import math

f = open('B-small-attempt0.in', 'r')
output = open('output.txt', 'w')

numTrials = int(f.readline())
for x in range(numTrials):
    NonEmptyPancakes = int(f.readline().rstrip())
    PancakePlates = [int(u) for u in f.readline().rstrip().split()]
    InitialAnswer = max(PancakePlates)
    NewAnswer = InitialAnswer
    summation = 0
    for y in range(1,InitialAnswer):
        for plate in PancakePlates:
            if plate > y:
                if plate % y == 0:
                    summation+= int((plate / y) - 1)
                else:
                    summation+= int(math.floor(plate / y))
        NewAnswer = int(min(NewAnswer, y + summation))
        summation = 0
    output.write("Case #" + str(x+1) + ": " + str(NewAnswer) + "\n")

output.close()
f.close()
    
