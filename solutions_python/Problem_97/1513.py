

def count_recycled(a, b):
    n = a
    m = a+1
    count = 0
    digits = len(str(n))
    for i in range(n, b+1):
        for j in range(i+1, b+1):
            for k in range(1, digits):
                if str(j)[k:] + str(j)[:k] == str(i):
                    count = count + 1
                    continue
    return count

def myfunc(myinput):
    myoutput = open("recycled.txt", "w")
    linenum = -1
    mystr = ""
    for line in open(myinput, "r"):
        linenum = linenum + 1
        if linenum == 0: continue
        mystr += "Case #%d: " % (linenum)
        nums = line.split()
        mystr += str(count_recycled(int(nums[0]), int(nums[1]))) + '\n'
    print mystr
    
myfunc('C-small-attempt1.in')
