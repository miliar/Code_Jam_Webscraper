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
    case = read_ints()
    dist, horses = case[0], case[1]
    return (dist, horses)

def write_case(i, res):
    print 'Case #' +str(i)+ ': ' + str(res)


#..............................................................................

#global variables


def begin():
    T = read_int()
    for i in range(1,T+1):
        case = read_case()
        res = solver(case)
        write_case(i, res)



#..............................................................................


def solver(case):
    distance = case[0]
    maxTime = -1
    for i in xrange(case[1]):
        horse = read_ints()
        time = float(distance - horse[0])/float(horse[1])
        if(time > maxTime or maxTime == -1):
            maxTime = time
    speed = float(distance)/maxTime
    return speed

begin()
