#!/usr/bin/env python



inFile = open("input.txt", 'r')

data = inFile.readlines()

data = [line.strip("\n") for line in data]

def solveProblem(pancakes, panSize):
    n = 0
    num = len(pancakes)
    
    for i in range(len(pancakes) - panSize + 1):
        if pancakes[i] == '-':
            pancakes = flip(pancakes, panSize, i)
            n +=1
    
    if('-' in pancakes):
        n = 'IMPOSSIBLE'
    return [n]

def flip(pancakes, panSize, i):
    flipped = ''
    for pancake in pancakes[i:(i+panSize)]:
        if pancake == '-':
            flipped += '+'
        else:
            flipped += '-'
    return pancakes[:i] + flipped + pancakes[(panSize + i):]


nInputs = data[0]
data.pop(0)

results = []

for line in data:
    a, i = line.split(" ")
    results += solveProblem(a, int(i))


outFile = open("output.txt","w") 

for i in range(int(nInputs)):
    line = "Case #{}: {}\n".format(i + 1, results[i])
    outFile.write(line)
    print(line.strip("\n"))
 
outFile.close()


