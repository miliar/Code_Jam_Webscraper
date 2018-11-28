import math
def output (N):
    while (not isTidy2 (N)):
        #print (N)
        N=adjustNumber2 (N)
    return N
'''
def output1( N):
    while (not isTidy (N)):
        N-=1
    return N

'''
def adjustNumber2 (N):
    a = list(str (N))
    flag = False
    for i in range (0, len(a)-1):
        if (flag):
            a[i] = "9"
        if (not flag and int (a[i]) > int (a[i+1])):
            a[i] = str(int (a[i])-1)
            flag = True
    if (flag):
        a[len (a)-1] = "9"
    return int ("".join(a))
            
def isTidy2 (N):
    while (N > 9):
       a = (str (N)[:-1])
       if (a == ""):
           newN = 0
       else:
           newN = int (a)
       if (N%10 < newN%10):
           return False
       N = newN
    return True

'''
def isTidy (N):
    while (N > 9):
       newN = int (N/10)
       #print (newN)
       if (N%10 < newN%10):
           return False
       N = newN
    return True
 '''          
    
def getInput ():
    array = []
    with open('B-large.in.txt') as f:
        l = [int(x) for x in next(f).split()]
        i = 1
        for line in f: # read rest of lines
            array = []
            array.append([int(x) for x in line.split()])
            #print (str (array[0]))
            print ("Case #" +str(i) + ": " + str(output(array[0][0])))
            #print ("Case #" +str(i) + ": " + str(output1(array[0][0])))
            i+=1

getInput()
