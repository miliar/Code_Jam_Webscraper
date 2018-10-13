import math

def isPalindrome(x):
    string = str(x)
    for x in range(0, len(string)/2):
        if (string[x] != string[len(string)-x-1]):
            return 0
    return 1

tries = raw_input()

for i in range(0, int(tries)):
    values = raw_input().split()
    sum = 0
    for x in range(int(values[0]), int(values[1])+1):
        if (isPalindrome(x) == 1 and math.sqrt(x)%1 == 0 and isPalindrome(int(math.sqrt(x))) == 1):
            sum += 1
    print "Case #" + str(i+1) + ": " + str(sum)