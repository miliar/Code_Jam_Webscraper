import string
import numpy as np
import math
from operator import itemgetter

def ispalindrome(word):
    return word == word[::-1]


def issquar(num2) :
    outcome = 0
    num = float(num2)
    if num > 0:
        num = (math.sqrt(num))
        inter = int(num)
        if num == inter:
            num2 = str(inter)
            if ispalindrome(num2) : 
                outcome = 1
        else:
            outcome = 0
        return outcome == 1       

lines = [line.strip() for line in open('C-small-attempt0.in')]
case = lines[0]
out = ''

table = string.maketrans("", "")
vert = 0
horl = 0
newcase = 1 
eachVert = 0
eachHorl = 0
ll = []
big_stokes = np.array([])
for k in range (len(lines)) :
    if (k != 0) :
        print k
        sentence = lines[k]     
        list = sentence.split(' ')
        start = int(list[0])
        end = int(list[1])
        end = end + 1
        result = 0
        for num in range(start,end):
            squarCheck = issquar(num)
            num = str(num)
            palinCheck = ispalindrome(num)
            if (squarCheck and palinCheck) : 
                result = result + 1
        print result
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        out += "Case #" + str(k) + ": " + str(result) + "\n"
        with open ('output', 'w') as f: 
            f.write (out)
        
        

