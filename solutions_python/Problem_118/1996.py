import os
from math import ceil, floor, sqrt

def setter(input=None):
    """ Read input file and return case in order
    
    """
    cases = int(input.readline())
    for case in xrange(cases):
        interval = map(int, input.readline().split())
        yield case+1, interval


def pdcheck(target=None):
    """ Check target string is palindrome or not
    
    """
    target = str(target)
    if  target[int(floor(len(target)/2.0)):] == target[:int(ceil(len(target)/2.0))][::-1]:
        return True
    else:
        return False


# location of input file
os.chdir(r'D:\ypsun\codejam\2013\Qualification Round\C. Fair and Square')
job = 'C-small-attempt0'

input = open(job + '.in', 'r')
output = open(job + '.out', 'w')
for case, interval in setter(input):
    s = int(ceil(sqrt(interval[0])))
    e = int(sqrt(interval[1])) + 1
    count = 0
    for num in xrange(s, e):
        if pdcheck(str(num)) and pdcheck(str(num**2)):
            count += 1
    output.write("Case #%(case)s: %(count)s\n" % locals())
input.close()
output.close
    
    
    