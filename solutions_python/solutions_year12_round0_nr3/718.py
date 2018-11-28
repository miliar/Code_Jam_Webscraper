from collections import deque

def breakIntoDigits(A):
    x = A
    out = []
    while x != 0:
        out.append(x%10)
        x/=10
    return [x for x in reversed(out)]
def makeANumber(l):
    n = 10**(len(l)-1)
    num = 0
    a = 0
    while n != 0:
        num += l[a] * n
        n/=10
        a+=1
    return num


def countRecycledPairs(A, B):
    num = A
    total = 0
    done = {}
    while num <= B:
        digits = breakIntoDigits(num)
        d = deque(digits)
        numRotated = 0
        rotatedNum = makeANumber(d)
        while numRotated<len(d):
            d.rotate(1)
            numRotated+=1
            rotatedNum = makeANumber(d)
            if num < rotatedNum and rotatedNum <= B and rotatedNum >= A and (num, rotatedNum) not in done:
                total+=1
                done[(num, rotatedNum)] = 1
        num+=1
    return total

    # go through, while our number is less than our current, rotate list around...

T = int(raw_input())
for x in range(T):
    line = raw_input().split()
    A = int(line[0])
    B = int(line[1])
    
    numRecycledPairs = countRecycledPairs(A, B)
    print "Case #" + str(x+1) + ": " + str(numRecycledPairs)
