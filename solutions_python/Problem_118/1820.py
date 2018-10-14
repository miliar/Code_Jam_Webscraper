import sys
import math

def palindrome(i):
    s = str(i)
    i = 1
    for c in s[:(len(s)/2)+1]:
        if c != s[-i]:
            return 0
        i = i + 1

    return 1

l = []
for i in range(1,int(math.sqrt(100000000000000))+1):
    if (palindrome(i) and palindrome(i*i)):
        l.append(i*i)

sys.stdin.readline()
line_number = 1
count = 0
for line in sys.stdin:
    if len(line.strip()) == 0:
        continue
    a = float(line.strip().split(' ')[0])
    b = float(line.strip().split(' ')[1])
    count = map(lambda x: 1 if x >= a and x <= b else 0, l).count(1)
    print "Case #" + str(line_number) + ": " + str(count)
    count = 0
    line_number = line_number + 1
