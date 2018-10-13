## Code by Preston Hamlin for CodeJam 2013
## prestonwhamlin@gmail.com

## Taking the square root of every number in the range would be bothersome and
##   require converting floats to ints and checking. Instead, run from 1 to
##   the root of the largest bound and generate a list of palindromes. This is 
##   certainly better than generating a list of palindromes for every test
##   case as well as faster than going through linearly.

from math import sqrt

## Returns True if s is a palindromes, False if not. s is a string.
def IsPalindrome(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if (s[0] == s[-1]):  ## if ends match, keep checking
        return IsPalindrome(s[1:-1])
    else:                ## if not, then not a Palindrome
        return False

def BSearch(val, some_list):
    high  = len(some_list)
    low   = 0
    pivot = 1
    old   = 0
    iters = 0
    
    ##print "Looking for " + str(val)
    while(True):
        if (iters > 50):
            break
        if (pivot == old):              ## if done searching
            return low                  ## return index
            
        old = pivot
        pivot = (high + low)/2
        ##print(high, low, pivot)
        
        if (val > some_list[pivot]):    ## throw out lower half
            low = pivot
        elif (val < some_list[pivot]):  ## throw out top half
            high = pivot
        iters += 1
            
            
ifile = open("input.txt", "r")
ofile = open("output.txt", "w")

result_list = []    
end = 0        
num_cases = int(ifile.readline())
endpoints = []

palindrome_list = []                   ## list of palindrome INTS
fs_list = []                           ## list of F&S INTS

## get test cases and endpoint
for case in range(num_cases):
    tmp = ifile.readline().split(' ')
    tmp[0] = int(tmp[0])
    tmp[1] = int(tmp[1])
    if tmp[1] > end:                   ## if range extended, update end
        end = tmp[1]
    endpoints.append(tmp)
    

    
    
## get palindromes between 1 and endpoint
for x in xrange(1, (int(sqrt(end) +1))):
    if IsPalindrome(str(x)):
        palindrome_list.append(x)
        ##print str(x) + " is a palindrome"
        
## get palindromes that are squares of palindromes (fair and square)
for pal in palindrome_list:            ## for each palindrome,
    x = pal*pal                        ## get its square
    if IsPalindrome(str(x)):           ## and check if palindrome
        print str(x) + " is a Fine Square Palindrome"
        fs_list.append(x)
    
## for each test case, do a binary search for each endpoint and get range
for points in endpoints:
    left  = 0
    right = 0
    size  = 0
    L_inclusive = False
    R_inclusive = False
    
    if points[0] in fs_list:
        left  = fs_list.index(points[0])
        L_inclusive = True
    if points[1] in fs_list:
        right = fs_list.index(points[1])
        R_inclusive = True
    if (L_inclusive):
        size += 1                      ## special case due to inclusive bounds
        
        
    if left == 0:
        left = BSearch(points[0], fs_list)
    if right == 0:
        right = BSearch(points[1], fs_list)
    
    size += right - left

    result_list.append(size)
    
## log results
for case in range(num_cases):
    ofile.write("Case #" + str(case +1) + ": " + str(result_list[case]) + '\n')

print
print fs_list
print "\nFINISHED"

ifile.close()
ofile.close()
