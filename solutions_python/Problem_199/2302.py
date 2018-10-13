INPUT_FILE_NAME = "A-large.in"
OUTPUT_FILE_NAME = "A-large.out"

def isHappy(row):
    if '-' in row:
        return False
    else:
        return True

def flip(row, k, start):
    for pancake in range(start, start + k):
        if row[pancake] == '+':
            row[pancake] = '-'
        else:
            row[pancake] = '+'
    

if __name__ == "__main__":
    inputFile = open(INPUT_FILE_NAME, 'r')
    outputFile = open(OUTPUT_FILE_NAME, 'w')

    numCases = int(inputFile.readline())

    for case in range(0, numCases):
        prob = inputFile.readline().split()
        k = int(prob[1])
        row = list(prob[0])
        count = 0
        pancakes = len(row)
        impossible = False
        print("Case #" + str(case+1))
        while isHappy(row) != True and impossible != True:
            for pancake in range(0, pancakes-k+1):
                if row[pancake] == '-':
                    flip(row, k, pancake)
                    count = count + 1
                    break
                if '-' in row[-k:] and pancake == pancakes-k:
                        impossible = True
                        break
        if impossible:
            outputFile.write("Case #" + str(case + 1) + ": IMPOSSIBLE\n")
        else:
            outputFile.write("Case #" + str(case + 1) + ": " + str(count) + "\n")

    print("End")
    inputFile.close()
    outputFile.close()

# outputFile.write("Case #" + str(case) + ": " + str(i+1) + " " + str(j+i+2) + "\n")
