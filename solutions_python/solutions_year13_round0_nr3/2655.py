import sys, math

finput = sys.stdin


def getlims(s):
    return map(int,s.split(' '))

def palendrome(i):
    if i or i==0:
        s = str(i)
        size = len(s)//2
        if size==0 : return True
        else       : return s[:size]==s[-size:][::-1]
    else: return False

def sqrt(i):
    retval = math.sqrt(i)
    if retval == int(retval) : 
        return int(retval)
    else :
        return False

def checks(A,B):
    c = 0
    for x in range(A,B+1):
        if palendrome(x):
            if palendrome(sqrt(x)):
                c+=1
    return c
"""
    nums = range(A,B)
    pals = [x for x in nums if palendrome(x)]
    c = 0
    for x in pals:
        if palendrome(sqrt(x)):
            c+=1
    return c
"""

def main():
    for test in xrange(int(finput.readline())):
        [A,B] = getlims(finput.readline())
        
        print "Case #{0:1d}:".format(test+1),
        print checks(A,B)


if __name__ == "__main__":
    main()
