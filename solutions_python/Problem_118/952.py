# Google Code Jam 2013 Qualification Round Problem C.
# Save intervals computed for previous (of 10000) problems.
# Find palindromes in range (sqrt(start), sqrt(end)), increment answer
# if their squares are palindromes.
# 900-100: 909 919 929 ... 999
# 12345-20000: 12421 12521 12621 ... 12921 13031 13131 13231 ... 13931
# 14041 14141 14241 ... 14941 15051 15151 15251 ... 15951 16061
# ... 99099 ... 99999
# So, 10 as middle digit varies.
# Generate palindromes, test if square of int is a palindrome.
import sys
import math
def palindromic(num):
    s = str(num)
    return s == s[::-1]

# count up until overflow into more digits
def incr(val):
    origLen = len(val)
    #if origLen == 0: return
    while True:
        if len(val) > origLen: return
        yield val
        if val == '': return
        val = str(int(val) + 1)

def genpalindromes(start):
    startInt = int(start)
    s = str(startInt)
    p = s[:len(s)/2]            # prefix
    while True:
        if len(s) % 2 == 0:
            for p in incr(p):
                result = int(p + p[::-1])
                if result >= startInt: yield result
            p = str((int(p)+1)/10)
        for p in incr(p):
            for center in '0123456789':
                result = int(p + center + p[::-1])
                if result >= startInt: yield result
        p = str((int(p) if p <> '' else 0) + 1)
        s = ''                  # do even case next
        centers = '0123456789'

# def genpalindromes(start):
#     val = int(start)
#     while True:
#         s = str(val)
#         if s == s[::-1]:
#             yield val
#         val += 1

def doCase(interval):
    answer = 0
    stop = math.sqrt(interval[1])
    for p in genpalindromes(math.ceil(math.sqrt(interval[0]))):
        if p > stop: return answer
        if palindromic(p*p):
            answer += 1
    
def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        answer = doCase(map(int, file.readline().split()))
        print 'Case #{0}: {1}'.format(case, answer)
run()
