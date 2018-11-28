
import sys
import math



def mul(x, y):
    return x * y

def sumprod(x, y):
    return sum(map(mul, x, y))


if __name__ == '__main__':

    for arg in sys.argv:
        inputfilename = arg;

    #check if input string is null???

    inputfile = open(inputfilename, 'r')

    outputfile = open(inputfilename + ".out", 'w')
    numberofsets = int(inputfile.readline())

    for m in range(numberofsets):


        #n = int(inputfile.readline().rstrip('\r\n')) #length of vector
        #print n
        x = inputfile.readline().rstrip('\r\n')
        x = map(int, x.split(' '))
        print x
        count = 0
        for i in range(x[0],x[1] + 1):
            root = int(math.sqrt(i))
            checkA = str(i) == str(i)[::-1]
            checkB = i == int(math.sqrt(i)) ** 2
            checkC = str(root) == str(root)[::-1]


            if checkA and checkB and checkC:
                print i
                count += 1


        #Check Palindrome: phrase_letters == phrase_letters[::-1]

        outputline = "Case #" + str(m + 1) + ": " + str(count) + "\n"
        print outputline
        outputfile.write(outputline)

