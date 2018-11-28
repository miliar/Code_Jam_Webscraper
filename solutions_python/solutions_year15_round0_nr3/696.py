# Google Code Jam - Dijkstra

# Returns the string obtained from doing quarternion multiplication (not exhaustive)
def quatMult(a, b):
    # Just return b
    if a == '1':
        return b

    # Negative a
    elif len(a) > 1:
        # Get the non-negative value
        val = quatMult(a[1], b)

        if len(val) > 1:
            return val[1]
        else:
            return '-' + val

    # Same values
    elif a == b and (a == 'i' or a == 'j' or a == 'k'):
        return '-1'

    # Go through the other types
    elif a == 'i' and b == 'j':
        return 'k'
    elif a == 'i' and b == 'k':
        return '-j'

    elif a == 'j' and b == 'i':
        return '-k'
    elif a == 'j' and b == 'k':
        return 'i'

    elif a == 'k' and b == 'i':
        return 'j'
    elif a == 'k' and b == 'j':
        return '-i'

# Returns what the string is equivalent to
def getEquivalentChar(string):
    chars = list(string)

    # Start out with 1 since it doesn't affect the value
    value = '1'
    for i in chars:
        old = value
        value = quatMult(value, i)

    return value

prefix = './C/'
inputFile = open(prefix + 'C-small-attempt0.in', 'r')
outFile = open(prefix + 'out.out', 'w')

# Number of test cases
T = int(inputFile.readline())

# Read in each row
for counter in range(T):
    line = list(map(int, inputFile.readline().split()))

    # Number of characters in following line
    L = line[0]

    # How many times to repeat
    X = line[1]

    # The letters (removes last new line char)
    string = inputFile.readline()[:-1]

    # Repeat the string X times
    inputString = string * X

    # Need to split inputString into 3 separate strings that are equivalent to i, j, k

    # Start at the beginning of the string until you get a substring equivalent to i
    firstIndex = 0
    char = inputString[firstIndex]

    while char != 'i' and firstIndex < len(inputString) - 1:
        firstIndex += 1
        char = quatMult(char, inputString[firstIndex])

    # Keep going until you get a substring equivalent to j
    secondIndex = firstIndex + 1
    if secondIndex < len(inputString):
        char = inputString[secondIndex]

    while char != 'j' and secondIndex < len(inputString) - 1:
        secondIndex += 1
        char = quatMult(char, inputString[secondIndex])

    # Test the remaining chars and see if it's k
    lastSubstring = inputString[secondIndex + 1:]
    value = getEquivalentChar(lastSubstring)

    if value == 'k':
        ans ='YES'
    else:
        ans = 'NO'

    outFile.write("Case #" + str(counter+1) + ": " + ans + "\n")

outFile.close()
