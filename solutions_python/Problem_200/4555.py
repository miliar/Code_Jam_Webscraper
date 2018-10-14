import fileinput
import sys

def tidyNumber(slist):
    n = len(slist)
    f = -1
    if n == 1:
        return slist
    for i in xrange(n-1):
        if int(slist[i]) == int(slist[i+1]):
            f = i
        elif int(slist[i]) > int(slist[i+1]):
            if f == -1:
                f = i
            for j in xrange(f, i+1):
                slist[j] = str(int(slist[j]) - 1)
            for j in xrange(i+1, n):
                slist[j] = str(9)
            break
        else:
            f = -1
    return slist

first = 0
count = 1

f = open('/home/deepak/Downloads/output.txt','w');
sys.stdout = f
for line in fileinput.input('/home/deepak/Downloads/B-small-attempt3.in'):
    if first == 0:
        num = int(line)
        first = 1
        continue
    s = int("".join(i for i in tidyNumber(list(line.rstrip()))))
    print "Case #"+ str(count) + ": " + str(s)
    count += 1
f.close()
'''
    #line = "557"
'''
#s = int("".join(i for i in tidyNumber(list(line.rstrip()))))
#print "Case #"+ str(count) + ": " + str(s)
#count += 1