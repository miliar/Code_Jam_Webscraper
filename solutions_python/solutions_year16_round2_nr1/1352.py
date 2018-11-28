from collections import Counter
import string

inputFile = open("A.in")
outputFile = open("A.out", "w")

T = int(inputFile.readline())

def getPhoneNumber(text):
    counts = dict(Counter(list(text)))
    phoneNumber = dict.fromkeys(range(10))
    for letter in string.ascii_uppercase:
        if letter not in counts:
            counts[letter] = 0

    for i in range(10):
        phoneNumber[i] = 0

    phoneNumber[0] = counts["Z"]
    counts["Z"] -= phoneNumber[0]
    counts["E"] -= phoneNumber[0]
    counts["R"] -= phoneNumber[0]
    counts["O"] -= phoneNumber[0]

    phoneNumber[8] = counts["G"]
    counts["E"] -= phoneNumber[8]
    counts["I"] -= phoneNumber[8]
    counts["G"] -= phoneNumber[8]
    counts["H"] -= phoneNumber[8]
    counts["T"] -= phoneNumber[8]

    phoneNumber[3] = counts["H"]
    counts["T"] -= phoneNumber[3]
    counts["H"] -= phoneNumber[3]
    counts["R"] -= phoneNumber[3]
    counts["E"] -= phoneNumber[3]
    counts["E"] -= phoneNumber[3]

    phoneNumber[4] = counts["R"]
    counts["F"] -= phoneNumber[4]
    counts["O"] -= phoneNumber[4]
    counts["U"] -= phoneNumber[4]
    counts["R"] -= phoneNumber[4]

    phoneNumber[6] = counts["X"]
    counts["S"] -= phoneNumber[6]
    counts["I"] -= phoneNumber[6]
    counts["X"] -= phoneNumber[6]

    phoneNumber[2] = counts["W"]
    counts["T"] -= phoneNumber[2]
    counts["W"] -= phoneNumber[2]
    counts["O"] -= phoneNumber[2]

    phoneNumber[7] = counts["S"]
    counts["S"] -= phoneNumber[7]
    counts["E"] -= phoneNumber[7]
    counts["V"] -= phoneNumber[7]
    counts["E"] -= phoneNumber[7]
    counts["N"] -= phoneNumber[7]

    phoneNumber[5] = counts["F"]
    counts["F"] -= phoneNumber[5]
    counts["I"] -= phoneNumber[5]
    counts["V"] -= phoneNumber[5]
    counts["E"] -= phoneNumber[5]

    phoneNumber[1] = counts["O"]
    counts["O"] -= phoneNumber[1]
    counts["N"] -= phoneNumber[1]
    counts["E"] -= phoneNumber[1]

    phoneNumber[9] = counts["E"]
    counts["N"] -= phoneNumber[9]
    counts["I"] -= phoneNumber[9]
    counts["N"] -= phoneNumber[9]
    counts["E"] -= phoneNumber[9]
    
    for letter in string.ascii_uppercase:
        if counts[letter] != 0:
            print(text)

    returnText = ""
    for i in range(10):
        returnText += str(i) * phoneNumber[i]

    return returnText

for i, line in enumerate(inputFile):
    print("Case #" + str(i + 1) + ": " + getPhoneNumber(line.strip()))


