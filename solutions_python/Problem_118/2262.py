def memoize(f):
    # define "wrapper" function that checks cache for
    # previously computed answer, only calling f if this
    # is a new problem.
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]

    # initialize wrapper function's cache.  store cache as
    # attribute of function so we can look at its value.
    memf.cache = {}
    return memf


def is_square(x):
    if x==0:
        return False
    x = x ** 0.5
    return int(x) == x,int(x)

def is_palindrome(sr):
            if len(sr)==1 or len(sr)==0:
                        return True
            else:
                        if (sr[0]==sr[-1]):
                                    return is_palindrome(sr[1:-1])
                        else:
                                    return False


def solve(st):
    if (is_palindrome(str(st))==True):
        res,no=is_square(int(st))
        if res == True:
            if (is_palindrome(str(no))==True):
                return 1
    return 0
                
            


def test():
    ls = open('Asmall.in','r').read()
    lines = ls.split('\n')
    count = int(lines[0])
    for j in range(1,count+1):
        one_line=lines[j].split(' ')
        result=0
        for i in range (int(one_line[0]),int(one_line[1])+1):
            result+= solve(str(i))
        print "Case #%d: " % (j), result
        
    



                        
