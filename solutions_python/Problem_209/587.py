# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.


from operator import attrgetter
import math

testCase = int(input())  # read a line with a single integer
#testCase = 1



for i in range(1, testCase + 1):
    ready, need = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    #ready = 4
    #need = 2
    panCakeList = []


    for k in range(0,ready):
        rad, height = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        panCakeList.append([rad*rad*math.pi, rad*height*2*math.pi])




    currentTop = 0
    Top =0
    sum = 0
    maxNum = 0
    maxPos =0

    
    for m in range (0,need):
        for n in range(0,ready-m):
            Top = panCakeList[n][0] - currentTop
            if(Top<0):
               Top = 0
           
            if(maxNum<Top+panCakeList[n][1]):
                maxPos=n
                maxNum=Top+panCakeList[n][1]
                
        
        if (panCakeList[maxPos][0] - currentTop > 0):
            currentTop = panCakeList[maxPos][0]
        panCakeList.pop(maxPos)

        sum+=maxNum
        maxNum=0
        


    print("Case #%d: %.9f"%(i, sum))
    # check out .format's specification for more formatting options


