
import sys
import string
import math
from math import sqrt
from math import pow
from math import log10

data = sys.stdin.readlines()

nbSamples = int(data.pop(0))
#print "nbSamples: ", nbSamples

def isAPalindrome(x):
    if (x < 10):
        return 1

    # Build numbers
    rep = {}
    y = x

    log10 = int(math.ceil(math.log10(x+1)))

    for i in range(log10):
        rep[i] = y % 10
        y = y / 10

    if (log10 % 2 == 0):
        for i in range(log10 / 2):
            if rep[i] != rep[log10 - 1 -i]:
                return 0
    else:
        for i in range((log10 - 1)/ 2):
            if rep[i] != rep[log10 - 1 -i]:
                return 0

    return 1

def isAFairPalindrome(x):
    return isAPalindrome(int(math.sqrt(x))) and isAPalindrome(x)

def isASquare(x):
    y = math.sqrt(x)
    return (round(y) * round(y) == x)

def pow10(n):
    return int(math.pow(10, n))

def inv(n):
    ncopy = n
    log10 = int(math.ceil(math.log10(n+1)))
    ans = 0
    
    for i in range(log10):
        ans = ans * 10
        ans = ans + (ncopy % 10)
        ncopy = ncopy / 10

    return ans

currSample = 1

for sample in range(nbSamples):

    print "Case #" + str(currSample) + ":",
    currSample = currSample + 1
    
    n, m = map(int, data.pop(0).rstrip().split())

    logn = int(math.log10(math.sqrt(n))+1)
    logm = int(math.log10(math.sqrt(m))+1)

    # i will be the possible length of the square root
    min = int(log10(sqrt(n))+1)
    max = int(log10(sqrt(m))+1)

#    print "min max n m", min, max, n, m
    nbOK = 0
    listOK = []
    prepareList = 0
    
    # Prepare the list:
    if prepareList:
        for i in range(min, max+1):

            # Enumerate the palyndroms of this size
            if (i % 2 == 0):
                for y in range(pow10(i/2 - 1), pow10(i/2)):
                    z = y * pow10(i/2) + inv(y)
                    test = z * z
    #                print test, isAPalindrome(test), test >= n, test <= m
                    if isAPalindrome(test) and test >= n and test <= m:
                        nbOK = nbOK + 1
                        print test, "(", y, z, ")"
                        listOK.append(test)
        
            else:
                for y in range(pow10(i/2 - 1), pow10(i/2)):
                    for next in range(10):
                        z = (y * 10 + next) * pow10(i/2) + inv(y)
                        test = z * z
    #                    print test, isAPalindrome(test), test >= n, test <= m
                        if isAPalindrome(test) and test >= n and test <= m:
                            nbOK = nbOK + 1
                            print test, "(", y, z, ")"
                            listOK.append(test)
        print listOK

    listOK = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 400000080000004, 10000000200000001, 10002000300020001, 10004000600040001, 10020210401202001, 10022212521222001, 10024214841242001, 10201020402010201, 10203040504030201, 10205060806050201, 10221432623412201, 10223454745432201, 12100002420000121, 12102202520220121, 12104402820440121, 12122232623222121, 12124434743442121, 12321024642012321, 12323244744232321, 12343456865434321, 12345678987654321, 40000000800000004, 40004000900040004, 1000000002000000001, 1000220014100220001, 1002003004003002001, 1002223236323222001, 1020100204020010201, 1020322416142230201, 1022123226223212201, 1022345658565432201, 1210000024200000121, 1210242036302420121, 1212203226223022121, 1212445458545442121, 1232100246420012321, 1232344458544432321, 1234323468643234321, 4000000008000000004]

    for i in listOK:
        if i >= n and i <= m:
            nbOK = nbOK + 1
#            print i

    print nbOK

# palindrome of size x:
#       if x is even: 10^(x/2)
#       if x is odd: 10^((x-1)/2) * 10
# one could enumerate palindroms in the sqrt range, with 10^(x/2) --> around 10^3.5



