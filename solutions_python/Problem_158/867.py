import sys

N = int(sys.stdin.readline())
f = open("omino2.txt", 'w')

for n in range(1, N+1):
    line = sys.stdin.readline()
    numbers = line.split()
    X = int(numbers[0])
    R = int(numbers[1])
    C = int(numbers[2])

    results = {}

    results[(1,1,1)] = "GABRIEL"
    results[(1,1,2)] = "GABRIEL"
    results[(1,1,3)] = "GABRIEL"
    results[(1,1,4)] = "GABRIEL"
    results[(1,2,1)] = "GABRIEL"
    results[(1,2,2)] = "GABRIEL"
    results[(1,2,3)] = "GABRIEL"
    results[(1,2,4)] = "GABRIEL"
    results[(1,3,1)] = "GABRIEL"
    results[(1,3,2)] = "GABRIEL"
    results[(1,3,3)] = "GABRIEL"
    results[(1,3,4)] = "GABRIEL"
    results[(1,4,1)] = "GABRIEL"
    results[(1,4,2)] = "GABRIEL"
    results[(1,4,3)] = "GABRIEL"
    results[(1,4,4)] = "GABRIEL"
    
    results[(2,1,1)] = "RICHARD"
    results[(2,1,2)] = "GABRIEL"
    results[(2,1,3)] = "RICHARD"
    results[(2,1,4)] = "GABRIEL"
    results[(2,2,1)] = "GABRIEL"
    results[(2,2,2)] = "GABRIEL"
    results[(2,2,3)] = "GABRIEL"
    results[(2,2,4)] = "GABRIEL"
    results[(2,3,1)] = "RICHARD"
    results[(2,3,2)] = "GABRIEL"
    results[(2,3,3)] = "RICHARD"
    results[(2,3,4)] = "GABRIEL"
    results[(2,4,1)] = "GABRIEL"
    results[(2,4,2)] = "GABRIEL"
    results[(2,4,3)] = "GABRIEL"
    results[(2,4,4)] = "GABRIEL"
    
    results[(3,1,1)] = "RICHARD"
    results[(3,1,2)] = "RICHARD"
    results[(3,1,3)] = "RICHARD"
    results[(3,1,4)] = "RICHARD"
    results[(3,2,1)] = "RICHARD"
    results[(3,2,2)] = "RICHARD"
    results[(3,2,3)] = "GABRIEL"
    results[(3,2,4)] = "RICHARD"
    results[(3,3,1)] = "RICHARD"
    results[(3,3,2)] = "GABRIEL"
    results[(3,3,3)] = "GABRIEL"
    results[(3,3,4)] = "GABRIEL"
    results[(3,4,1)] = "RICHARD"
    results[(3,4,2)] = "RICHARD"
    results[(3,4,3)] = "GABRIEL"
    results[(3,4,4)] = "RICHARD"
    
    results[(4,1,1)] = "RICHARD"
    results[(4,1,2)] = "RICHARD"
    results[(4,1,3)] = "RICHARD"
    results[(4,1,4)] = "RICHARD"
    results[(4,2,1)] = "RICHARD"
    results[(4,2,2)] = "RICHARD"
    results[(4,2,3)] = "RICHARD"
    results[(4,2,4)] = "RICHARD"
    results[(4,3,1)] = "RICHARD"
    results[(4,3,2)] = "RICHARD"
    results[(4,3,3)] = "RICHARD"
    results[(4,3,4)] = "GABRIEL"
    results[(4,4,1)] = "RICHARD"
    results[(4,4,2)] = "RICHARD"
    results[(4,4,3)] = "GABRIEL"
    results[(4,4,4)] = "GABRIEL"

    f.write("Case #" + str(n) + ": " + str(results[(X,R,C)]) + "\n")
f.close()
