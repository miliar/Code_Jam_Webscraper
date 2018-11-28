import string
import math
#daniel hammack
def processfile(path):
    fout = open(string.replace(path,'in','out'), 'w')
    with open(path,'r') as f:
        lines = f.readlines()

    lines = [string.replace(l,'\n', '') for l in lines]
    #lines = [l for l in lines if len(l) > 0]
    cases = int(lines[0])
    for i in range(0,cases):
        items = lines[i+1].split(' ')
        begin, end = int(items[0]), int(items[1])
        fout.write('Case #' + str(i+1) + ': ' +
                   str(count_fair_and_square(begin, end)) + '\n')
            
    fout.close()


def count_fair_and_square(begin, end):
    #the idea - check square nums in the range.
    ibegin, iend = int(math.ceil(begin ** .5)), int(math.ceil(end ** .5))
    #we only want numbers {X : p(X) and p(X^2)} where p = palindrome
    count = 0
    for smallnum in xrange(ibegin, iend+1):
        if ispalindrome(smallnum):
            if ispalindrome(smallnum ** 2):
                if begin <= smallnum ** 2 <= end:
                    count += 1
    return count

def ispalindrome(int_num):
    s = str(int_num)
    le = len(s)
    for i in xrange(0, int(le/2)):
        if s[i] != s[-i-1]:
            return False
    return True

processfile('C:\\users\\daniel\\desktop\\c-small-attempt0.in')
