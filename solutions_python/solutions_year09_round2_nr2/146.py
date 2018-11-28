import math
import sys

def get_count(n):
    count = [0, 0, 0, 0, 0,
             0, 0, 0, 0, 0]
    while (n):
        if (n%10) != 0:
            count[n%10] = count[n%10] + 1
        n/=10

    return count

def match_counts(count1, count2):
    for i in range(1, 10):
        # print i
        # print str(count1[i]) + ", " + str(count2[i])
        if count1[i] != count2[i]:
            return False;
    return True
    
    
t = int(raw_input())
ctr = 1
while (t != 0):
    t = t - 1
    n = int(raw_input())
    oldn = n
    oldc = get_count(oldn)
    n = n + 1
    # print "n == " + str(n)
    while (match_counts(oldc, get_count(n)) == False):
        n = n + 1

    print "Case #" + str(ctr) + ": " + str(n)
    ctr = ctr + 1


    
