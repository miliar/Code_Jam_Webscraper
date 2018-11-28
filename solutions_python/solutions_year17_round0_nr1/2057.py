import sys

def main():
    if(len(sys.argv) < 2):
        print("Not enough arguments. Exiting.")
        exit()
    file = open(sys.argv[1], 'r')

    totalCases = int(file.readline().strip())
    testCases = 0

    line = file.readline().strip()
    while(line != ""):
        pancakes, flipper = line.split(" ")
        pancakes = list(pancakes)
        flipper = int(flipper)
        testCases += 1
        flips = 0

        for i in range(len(pancakes) - flipper + 1):
            if(pancakes[i] == '-'):
                flips += 1
                for j in range(i, i + flipper):
                    if(pancakes[j] == '-'):
                        pancakes[j] = '+'
                    else:
                        pancakes[j] = '-'

        if(all(pancake == '+' for pancake in pancakes)):
            print("Case #" + str(testCases) + ": " + str(flips))
        else:
            print("Case #" + str(testCases) + ": IMPOSSIBLE")
        line = file.readline().strip()

    file.close()

if(__name__ == "__main__"):
    main()
