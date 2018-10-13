import time
#500 4 2000
def print7dp(ilist):
    for i in ilist:
        print "%0.7f" %i
    #print ["%0.7f" % i for i in ilist]

def secondToWin(inc, inf, inx):
    #create Table
    approimate = 100000
    cr = 2.0
    table = []
    subt1 = []
    subt2 = []
    for i in range(0,approimate):
        subt1.append(inc/cr)
        subt2.append(inx/cr)
        cr = cr + inf
    #table.append(subt1)
    #table.append(subt2)
    #print7dp(subt1)
    #print7dp(subt2)

    if(subt1[0] > subt2[0]):
        return subt2[0]
    
    index = 1
    pervious_second = subt2[0]
    cumulative_second = subt1[0]
    while(True):
        current_second = cumulative_second + subt2[index]
        cumulative_second = cumulative_second + subt1[index]
        index = index + 1
        #print current_second , pervious_second
        if(current_second > pervious_second):
            return pervious_second
        pervious_second = current_second

    
    

infile = open("B-large.in","r")
y = infile.readline()
y = y.split()
N  = int(y[0])

for i in range(0,N):
    start = time.clock()
    temp = []
    y = infile.readline()
    y = y.split()
    c = float(y[0])
    f = float(y[1])
    x = float(y[2])
    result = secondToWin(c, f, x)
    s = "Case #" + str(i+1) + ":"
    print s,"%0.7f" % result
    end = time.clock()
    #print "Time : ", (end - start)
    
