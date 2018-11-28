
import sys

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
        n = int(inputfile.readline().rstrip('\r\n')) #length of vector
        print n
        x = inputfile.readline().rstrip('\r\n')
        x = map(int, x.split(' '))
        print x
        x.sort()


        patrick = x[0] #always give patrick the lowest value candy
        sean = sum(x) - patrick
        xor = 0

        for count in range(len(x)):
            if (x == 0):
                xor = x[0]
            else:
                xor ^= x[count] #xor
            print "xor is: " + str(xor)


        if (xor == 0):
            result = str(sean)
        else:
            result = "NO"

        outputline = "Case #" + str(m + 1) + ": " + result + "\n"
        print outputline
        outputfile.write(outputline)




