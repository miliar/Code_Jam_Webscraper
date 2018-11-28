
import sys
import math


def do_something(n, k):
    print('-' * 10)
    print('n:', n)
    print('k:', k)
    if n != k:
        log = math.ceil(math.log(k + 1, 2))
        power = pow(2, log)
        est = (n - k) / power
        if ((n - k) % power) >= power / 2:
            maxi = math.ceil(est)
        else:
            maxi = math.floor(est)
        mini = int(math.floor(est))
        print('log:', log)
        print('estimate:', est)
        print('result:', maxi, mini)
        return maxi, mini
    else:
        print('result: 0, 0')
        return 0, 0

if __name__ == '__main__':

    for arg in sys.argv:
        inputfilename = arg

    inputfile = open(inputfilename, 'r')

    outputfile = open(inputfilename + ".out", 'w')
    numberofsets = int(inputfile.readline())

    #for i in range(1, 20):
    #    do_something(1000, i)


    for m in range(numberofsets):
        n, k = map(int, inputfile.readline().rstrip('\r\n').split(' '))
        maxi, mini = do_something(n, k)

        outputline = "Case #" + str(m + 1) + ": {} {}\n".format(maxi, mini)
        print(outputline)
        outputfile.write(outputline)

