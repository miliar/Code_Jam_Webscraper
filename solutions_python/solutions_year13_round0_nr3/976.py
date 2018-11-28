import math

def main():
    fileName = "C-small-attempt0.in"
    file = open(fileName)

    # Loop for the number of tests there are.
    for case in range(1, int(file.readline())+1):
        # Read in the endpoints.
        line = file.readline().split()
        lower = math.ceil(math.sqrt(int(line[0])))
        upper = math.floor(math.sqrt(int(line[1])))

        # Determine if each value is fair and square.
        count = 0
        for value in range(lower, upper+1):
            isValid = True

            # Check if the square root of the value is a palindrome.
            strValue = str(value)
            length = len(strValue)
            for index in range(length//2):
                if strValue[index] != strValue[length-1-index]:
                    isValid = False

            # Check if the value is a palindrome.
            strSquare = str(value**2)
            lengthSquare = len(strSquare)
            for index in range(lengthSquare//2):
                if strSquare[index] != strSquare[lengthSquare-1-index]:
                    isValid = False

            # If it is valid, then add it to the count.
            if isValid:
                count += 1
                
        # Print the number found.
        print("Case #" + str(case) + ": " + str(count))

if __name__ == "__main__":
    main()
