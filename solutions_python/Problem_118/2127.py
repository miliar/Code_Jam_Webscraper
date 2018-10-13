
import math

def isPalindrome(num):
    i = 0
    string = str(num)
    #print string
    if len(string) % 2 == 1:
        maximum = math.ceil(len(string)/2.0)
    else:
        maximum = len(string)/2+1
    #print maximum
    while i < maximum:
        if i == 0 and string[i] == "0":
            #print "Leading Zero"
            return False
        if string[i] != string[-(i+1)]:
            #print "Not Pally"
            return False
        i += 1
    #print "Pally"
    return True


def generator(start,stop):
    i = start
    while i <= stop:
        yield i
        i += 1

def problem2(start,stop):
    ##print "Start: "+str(start)
    ##print "Stop: "+str(stop)
    counter = 0
    for square in generator(start,stop):
        if isPalindrome(square):
            if math.sqrt(square) % 1 == 0 and isPalindrome(int(math.sqrt(square))):
                counter += 1
    return counter


f = open('p2_small.in','r')
w = open('problem2_output.txt','w')
counter = 0
for line in f:
    if counter == 0:
        numTests = int(line.strip())
    else:
        params = line.strip().split()
        ##print params
        ##print "Case #"+str(counter)+": "+ str(problem2(int(params[0]),int(params[1])))
        w.write("Case #"+str(counter)+": "+ str(problem2(int(params[0]),int(params[1])))+"\n")
    counter += 1
w.close()
f.close()
