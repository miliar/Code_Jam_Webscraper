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
    num=read_int()
    return (num)

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

def findBreak(s, l):
    brkPt = None
    for i in xrange(l-1):
        if int(s[i] > s[i+1]):
            brkPt = i
            break
    if (brkPt != None) and (brkPt != 0):
        z = brkPt
        while z!= 0:
            if int(s[z-1]) > (int(s[z])-1):
                z-=1
            else:
                break
        brkPt = z
    return brkPt



def solver(case):
    s = str(case)
    length = len(s)
    if(length == 1):
        return case
    pos = findBreak(s,length)
    if(pos == None):
        return case
    s = s[:pos] + str(int(s[pos])-1) + '9'*(length - pos - 1)
    if(s[0]) =='0':
        s = s[1:]
    return int(s)


begin()
