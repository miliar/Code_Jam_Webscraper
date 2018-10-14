def other(item):
    if item == 1:
        return 0
    else:
        return 1
    

def change(pattern, initial=0):
    last = initial
    np = []
    for item in pattern:
        # change
        if item == 1:
            last = other(last)
        else:
            last = last

        # add to end
        np.append(last)
    return np


def change2(pattern):
    np = []
    for index, item in enumerate(pattern):
        if index > 0:

            arr = filter(lambda x: x == 0, pattern[:index])
            #print index, arr
            if arr:
                np.append(pattern[index])
            else:
                np.append(other(pattern[index]))                
                
        else:
            np.append(1)
    return np

def pattern(i):

    if i == 1:
        return [1, 0]

    else:
        old_pattern = pattern(i - 1)

        pattern1 = change(old_pattern)
        if pattern1[-1] == 1:
            pattern2 = change(old_pattern, initial=1)
            pattern1 = pattern1 + pattern2

        return pattern1



def last(n, k):
    p = pattern(n)
    if k < n:
        return False
    else:
        index = k - n
        index = index % len(p)
        #print index
        return p[index] == 1


def last2(n, k):
    start = [1] + [0 for i in range(n)]

    #print "Seq"
    #print start
    for j in range(k):
        start = change2(start)
        #print j + 1, start[1:], start[-1] == 1
        print j + 1, start[1:]
    for i in start:
        if i == 0:
            return False
    return True

def last3(n, k):
    good = pow(2, n)
    return (k + 1) % good == 0

def solve(fname, solver=last):
    myfile = open(fname + ".in","r")
    myfile2 = open(fname + ".out","w")
    text = myfile.readlines()
    lines = int(text.pop(0))

    for i in range(lines):
        n, k = map(int, text.pop(0).split(" "))
        if solver(n, k):            
            answer = "ON"
        else:
            answer = "OFF"
        output = "Case #%d: %s\n" % (i + 1, answer)
        myfile2.write(output)


    

    
#for i in range(20):            
#    print last(5, i)

#last(1, 0)
print "Done"
solve("c:/large", solver=last3)
