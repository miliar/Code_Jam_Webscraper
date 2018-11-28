import sys
import math

basename  = sys.argv[0][0:-3]

#basename = basename + "-practice"
basename = "C-small-attempt1"

input_filename = basename + ".in"
output_filename = basename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

test_cases = int(input_file.readline().rstrip())

def evenpal(n):
    s = str(n)
    return int(s + str(''.join(reversed(s))))

def oddpal(n):
    s = str(n)[:-1]
    c = str(n)[-1]
    return int(s + c + str(''.join(reversed(s))))

def ispal(n):
    s = str(n)
    l = math.floor(len(s) / 2)
    return l == 0 or s[:l] == s[-l:]

# Code of smallest even-length palindrome bigger than n
def supeven(n):
    s = str(n)
    if len(s) % 2 == 1:
        newlen = int((len(s) + 1) / 2)
        result = int("1" + ''.join('0' for i in range(newlen - 1)))
    else:
        firsthalf = int(s[0:int(len(s)/2)])
        if evenpal(firsthalf) >= n:
            result = firsthalf
        else:
            result = firsthalf + 1
    return result

# Code of greatest even-length palindrome smaller than n
def infeven(n):
    s = str(n)
    if len(s) % 2 == 1:
        newlen = int((len(s)-1)/2)
        if newlen == 0:
            result = 0
        else:
            result = int(''.join('9' for i in range(newlen)))
    else:
        firsthalf = int(s[0:int(len(s)/2)])
        if evenpal(firsthalf) <= n:
            result = firsthalf
        else:
            result = firsthalf - 1
    return result

# Code of smallest odd-length palindrome bigger than n
def supodd(n):
    s = str(n)
    if len(s) % 2 == 0:
        newlen = int( (len(s)/2) ) + 1
        result = int("1" + ''.join('0' for i in range(newlen - 1)))
    else:
        code = int(s[:math.ceil(len(s)/2)])
        if oddpal(code) >= n:
            result = code
        else:
            result = code + 1
    return result

# Code of largest odd-length palindrome smaller than n
def infodd(n):
    s = str(n)
    if len(s) % 2 == 0:
        newlen = int( (len(s))/2 )
        if newlen == 0:
            result = 0
        else:
            result = int(''.join('9' for i in range(newlen)))
    else:
        code = int(s[:math.ceil(len(s)/2)])
        if oddpal(code) <= n:
            result = code
        else:
            result = code - 1
    return(result)

for case in range(1, test_cases+1):
    line = [int(i) for i in input_file.readline().rstrip().split()]
    A , B = line[0], line[1]

    lower = math.ceil(math.sqrt(A))
    upper = math.floor(math.sqrt(B))

    firsteven = supeven(lower)
    lasteven = infeven(upper)
    firstodd = supodd(lower)
    lastodd = infodd(upper)

    totaleven = max(0, lasteven - firsteven + 1)
    totalodd = max(0, lastodd - firstodd + 1)

#    print([evenpal(i)**2 for i in range(firsteven,lasteven+1)])
#    print([oddpal(i)**2 for i in range(firstodd,lastodd+1)])

    evens = len([i for i in range(firsteven, lasteven+1) if ispal(evenpal(i)**2)])
    odds = len([i for i in range(firstodd, lastodd+1) if ispal(oddpal(i)**2)])

#    print("A,B = " + str(A) + "," + str(B))
#    print("lower,upper = " + str(lower) + "," + str(upper))
#    print("first even = " + str(evenpal(firsteven)))
#    print("last even = " + str(evenpal(lasteven)))
#    print("first odd = " + str(oddpal(firstodd)))
#    print("last odd = " + str(oddpal(lastodd)))
#    print("total even = " + str(evens))
#    print("total odd = " + str(odds))

    output_file.write("Case #" + str(case) + ": " + str(evens+odds))
    if case < test_cases:
        output_file.write('\n')

