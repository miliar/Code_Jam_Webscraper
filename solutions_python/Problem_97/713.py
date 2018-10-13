import sys
import getopt
import re

def cycle(num,i):
    s = str(num)
    return s[i:] + s[:i]

def process(nums):
    A = nums[0]
    B = nums[1]

    count = 0

    d = [False]*(B-A+1)
    #checked = set()


    for n in range(A,B+1):
        #if (n-A) in checked:
        #    continue
        #checked.add(n-A)
        if d[n-A]:
            continue
        d[n-A] = True
        classy = [n]
        for ix in range(len(str(n))):
            tempnum = int(cycle(n,ix))
            if not len(str(tempnum)) == len(str(n)):
                continue
            if tempnum not in classy and tempnum >= A and tempnum <= B:
                classy.append(tempnum)                
                #checked.add(tempnum-A)
                d[tempnum-A] = True

        mylength = len(classy)
        if mylength < 2:
            continue
        count += mylength * (mylength-1)/2

    return count

if __name__ == "__main__":

    f = open('C-large.in','r')
    f.readline()
    i = 0

    #process([12345,12345])
    #sys.exit(0)


    for line in f:
        i = i+1
        pr = "Case #"
        pr += str(i)
        pr += ": "
        
        nums = [int(x) for x in line.split()]
        
        pr += str(process(nums))
        print pr


    


