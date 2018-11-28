'''
Created on 30 apr. 2017

@author: windows7
'''
from sympy.interactive.tests.test_ipython import readline

def twoOrFour():
    A1 = input().split()
    A2 = input().split()
    
    if (int(A1[0]) < int(A2[0])):
        dist1 = int(A2[1]) - int(A1[0])
        dist2 = 1440 - int(A2[0]) + int(A1[1])
    else:
        dist1 = int(A1[1]) - int(A2[0])
        dist2 = 1440 - int(A1[0]) + int(A2[1])        
    if (dist1 <= 720):
        return "2"
    elif (dist2 <= 720):
        return "2"
    else:
        return "4"
    

def howManyChanges(activities):
    listActivities = activities.split()
#     a = int(listActivities[0])
#     b = int(listActivities[1])
#     c= a+b
    if ((int(listActivities[0])+int(listActivities[1])) == 1 ):
        input()
        return "2"
    elif ((int(listActivities[0]) == 1) and (int(listActivities[1]) == 1)):
        input()
        input()
        return "2"
    else:
        noChanges = twoOrFour()
        return noChanges


if __name__ == "__main__":
    # For final solution replace the following three lines
    # with t = int(input())
    
#     in_file = open('.\\sample.txt', 'r')
#     out_file = open('.\\sample.out', 'w')
#     
#     in_file = open('.\\input.txt', 'r')
#     out_file = open('.\\out.txt', 'w')
    t = int(input()) # Read first line

    for i in range(1, t + 1):
        # replace next line with n = input() to read one line
        n = input() # read one line    
        tidyNum = howManyChanges(n)
        
        # replace next line with print("Case #{}: {}".format(i, tidyNum)")
        # i.e. the same within print as in write except the new-line-cmd
        print ("Case #{}: {}".format(i, tidyNum))
        
#     #Remove close-statements
#     in_file.close()
#     out_file.close()