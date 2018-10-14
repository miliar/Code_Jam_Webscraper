# Google Code Jam 2017, Qualification round solution 
# NILANJAN BALA, kylemills007@gmail.com

from itertools import permutations #For generating all the permutations

cases = int(input())

def change(alist, start, end): 
   """Given a list with start and end points, it reverses all the elements i.e if + then -, if - then + """
   for i in range(start, end):
        if(alist[i]=='+'):
            alist[i]= '-'
        else:
            alist[i] = '+'

# def clearList(aList, pansize):
#     """Given a list it returns the no of groups of '-' which occurs pansize no of times consecutively
#     and removes the groups of '+' and '-' which occur pansize no of times"""
#     counter = 0
#     i = 0
#     while(i < len(pancakeList) - pansize ):
#         # print(aList)
#         if((pancakeList[i] == '-' and pancakeList[i+1] == '-' and pancakeList[i+2] == '-')):
#             del pancakeList[i:i+3]
#             counter = counter +1

#         else :
#             i = i+1
#     return counter


# Check for all the elements in input
for n in range(0,cases):
    pancakes, pansize = input().split(' ')
    pansize = int(pansize)
    pancakeList = [no for no in pancakes]

    counter = 0
    # counter = clearList(pancakeList,pansize) # The pancakeList changes size so length is calculated after this
    length = len(pancakeList)

    plus = ['+' for f in range(length)] #List containing all '+' which is compared with for equality

# ---------------------------------
    i = 0
    mycounter = 0
    flag = False
    while(i < length - pansize+1):
        if(pancakeList[i] == '-'):
            change(pancakeList,i,i+pansize)
            mycounter = mycounter +1
        if(pancakeList == plus):
            flag = True
            break
        i= i+1
            
    if(flag == False):
        print("Case #{}: IMPOSSIBLE".format(n+1))
    else :
        print("Case #{}: {} ".format(n+1,mycounter+counter))

# ---------------------------------

    # permuteList = (permutations(range(0,length-(pansize-1)))) # Generator which gives the permutations one by one
    # flag = 0 # To indicate if the first time generator expression is used
    # rev = () # Holds the reverse of the first permutation
    # minimum = length + 1
    # pos = -1

    # # Here its checked if for a given permutation the list generated is equal to plus
    # while permuteList:
    #     ele = permuteList.__next__()
    #     if(flag == 0):
    #         flag = 1
    #         rev = tuple(sorted(ele, reverse =True))


    #     templist = [no for no in pancakeList] # A temporary list for making changes and comparing
    #     if(templist == (plus)):
    #         minimum = -1
    #     else :
    #         for i,a in enumerate(ele):
    #             pos = int(a)
    #             change(templist,pos,pos+pansize)
    #             if(templist == (plus)):
    #                 if(i < minimum):
    #                     minimum = i
    #                 break

    #     if(ele == rev):
    #         break
    # #
    # if(minimum == length+1):
    #     print("Case #{}: IMPOSSIBLE".format(n+1))
    # else :
    #     print("Case #{}: {} ".format(n+1,minimum+1+counter))
