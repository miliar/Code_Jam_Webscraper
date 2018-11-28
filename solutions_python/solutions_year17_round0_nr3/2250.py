import math

def read_word():
    return raw_input()

def read_int(b=10):
    return int(read_word(), b)

def read_letters():
    return list(read_word())

def read_digits(b=10):
    return [int(x, b) for x in read_letters()]

def read_words(d=' '):
    return read_word().split(d)

def read_ints(b=10, d=' '):
    return [int(x, b) for x in read_words(d)]

def read_floats(d=' '):
    return [float(x) for x in read_words(d)]


#..............................................................................


def read_case():
    num=read_ints()
    return num

def write_case(i, res):
    print 'Case #' +str(i)+ ': ' + str(res)


#..............................................................................

#global variables


def begin():
    T = read_int()
    for i in xrange(1,T+1):
        case = read_case()
        res = solver(case)
        write_case(i,res)

#..............................................................................

def solver(case):
    N,k = case[0],case[1]
    partitions = int(math.pow(2,int(math.log(k,2))))
    toilets = N - partitions + 1
    minSize = int(toilets/partitions)
    maxSize = minSize + 1
    maxNum = toilets - minSize*partitions
    minNum = partitions - maxNum
    more_to_fill = k - partitions + 1
    if more_to_fill <= maxNum:
        if maxSize%2 == 0:
            return str(int(maxSize/2)) + " " + str(int(maxSize/2)-1)
        else:
            return str(int(maxSize/2)) + " " + str(int(maxSize/2))
    else:
        if minSize%2 == 0:
            return str(int(minSize/2)) + " " + str(int(minSize/2)-1)
        else:
            return str(int(minSize/2)) + " " + str(int(minSize/2))

begin()
