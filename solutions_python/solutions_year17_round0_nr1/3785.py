import sys


infile = open("A-large.in", 'r');
#f = open("output.txt", 'w+');

def func(myStr, K):
    myStr = list(myStr)
    size = len(myStr)
    if (size < K):
        return -1
    counter = 0
    for i in range(0,size):
        if myStr[i] == '-':
            if ((size -i) >= K):
                counter += 1
                for j in range(0,K):
                    if (myStr[i+j] == '-'):
                        myStr[i+j] = '+'
                    elif (myStr[i+j] == '+'):
                        myStr[i+j] = '-'
            else:
                return -1
                
    return counter;
                        
    

def mymain(T):    
    for i in range(0,int(T)):
        tLine = infile.readline().rstrip()
        myArr = tLine.split()
        tResult = func(myArr[0], int(myArr[1]))
        if (tResult != -1):
            print "Case #" + str(i+1) +": "+ str(tResult)
        if (tResult == -1):
            print "Case #" + str(i+1) +": IMPOSSIBLE"


T = infile.readline().rstrip();
#print len(T);

mymain(T)