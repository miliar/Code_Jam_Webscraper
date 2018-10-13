def parse_input(filename):
    return [i.strip() for i in open(filename).readlines()][1:]

def findMostRecentTidyNumber(num):
    numToCheck = [int(i) for i in list(str(num))]
    
    # Iterate backwards through the numbers
    # Check if number[i-1] < number[i]
    # If so, decrement that number, and change all the following numbers to 9

    for index in range(len(numToCheck) - 1, 0, -1):
        digit = numToCheck[index]
        previousDigit = numToCheck[index - 1]
        if previousDigit > digit:
            numToCheck[index - 1] -= 1
            for secondIndex in range(index, len(numToCheck), 1):
                numToCheck[secondIndex] = 9

    num = int(''.join([str(i) for i in numToCheck]))
    return num


def main():
    inputFile = "B-large.in"
    nums = parse_input(inputFile)
    outputFile = inputFile.split(".")[0] + ".out"
    with open(outputFile, 'w') as f:
        for index in range(len(nums)):
            f.write("Case #{0}: {1}\n".format(index + 1, findMostRecentTidyNumber(nums[index])))

main()