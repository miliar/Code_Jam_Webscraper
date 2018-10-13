import math

def main(pancakes, k, trial, output):
    if '-' not in pancakes:
        output.write("Case #" + str(trial) + ": 0\n")
    else:
        flips = 0
        for x in range(0, (len(pancakes)-k)+1):
            if (pancakes[x] == '-'):
                flips += 1
                minusmax = 0
                plusmax = 0
                for y in range(x, x+k):
                    if pancakes[y] == '-':
                        pancakes[y] = '+'
                    else:
                        pancakes[y] = '-'
        print(pancakes)
        if '-' in pancakes:
            output.write("Case #" + str(trial) + ": IMPOSSIBLE\n")
        else:
            output.write("Case #" + str(trial) + ": " + str(flips) + "\n")

def init():
    n = int(raw_input())
    output = open("output.txt", "w")
    for trial in range(1, n+1):
        myInput = str(raw_input())
        myInputString = myInput.split(" ")
        pancakes = list(myInputString[0])
        k = int(myInputString[1])
        main(pancakes, k, trial, output)
    output.close()

init()
