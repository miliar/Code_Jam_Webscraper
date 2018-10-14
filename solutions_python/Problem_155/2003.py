
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
        x = inputfile.readline().rstrip('\r\n')
        (length, values) = map(str, x.split(' '))

        count = 0
        cum_sum = 0
        for i in range(int(length)+1): #should be up to length
            val = int(values[i])
            if val == 0:
                if (cum_sum <= i):
                    count += 1
                    cum_sum += 1
            cum_sum += val


        outputline = "Case #" + str(m + 1) + ": " + str(count) + "\n"
        print outputline
        outputfile.write(outputline)

