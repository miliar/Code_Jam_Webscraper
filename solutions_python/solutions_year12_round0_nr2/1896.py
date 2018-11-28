#-------------------------------------------------------------------------------
# Name:        Dancing With the Googlers
# Purpose:
#
# Author:      udonko
#
# Created:     14/04/2012
# Copyright:   (c) udonko 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
most = 0
def main():
    global most
    input = open("input.txt","r")
    output = open("output.txt","w")
    try:
        temp = input.readline()
        t = int(temp)
        for i in range(t):
            sys.stdout.write("-------\n")
            temp = input.readline()
            temp = temp.strip()
            temps = temp.split()
            n = int(temps[0])
            s = int(temps[1])
            p = int(temps[2])
            nums = []
            for j in range(n):
                nums.append( int(temps[3+j]) )
            nums.sort()
            nums.reverse()
            calc(n,s,p,nums)
            outtext ="Case #"+str(i+1)+": "+str(most)+'\n'
            output.write(outtext)
            sys.stdout.write(outtext)
    finally:
        input.close()
        output.close()
def isbiggerthan(triplets, flag, p):
    """ flag == false==> not surprizing """
    ret = triplets % 3
    num = triplets//3
    if flag == False:
        if ret != 0:
            num += 1
    else:
        # 0:0 1
        # 7: 1 3 3 mean = 2
        # 8: 2 2 4 mean=2
        if ret == 0:
            num += 1
        elif ret == 1:
            num += 1
        else:
            num += 2

    #sys.stdout.write(str(triplets)+" "+str(flag) +" p="+str(p)+"num="+str(num)+"-----\n")

    if num >= p:
        return True
    else:
        return False
# 1 3 3
# 0 1 2
# 0 0 2
def calc(n,s,p,nums):
    global most
    most = 0
    calc2(n,s,p,nums, 0, 0)
def calc2(n,s,p,nums, index, result):
    global most
    if index == len(nums):
        if s == 0:
            most = max(result, most)
            return
        else:
            return
    if nums[index] < 2 or  s ==0:
        if isbiggerthan(nums[index],False,p) == True:
            calc2(n,s,p,nums,index+1, result+1)
        else:
            if nums[index]//3+2 < p:
                #sys.stdout.write("cut\n")
                most = max(result, most)
            else:
                calc2(n,s,p,nums,index+1, result)
    else:
        if isbiggerthan(nums[index],True,p) == True:
            calc2(n,s-1,p,nums,index+1, result+1)
        else:
            if nums[index]//3+2 < p:
                #sys.stdout.write("cut\n")
                most = max(result, most)
            else:
                calc2(n,s-1,p,nums,index+1, result)
        if isbiggerthan(nums[index],False,p) == True:
            calc2(n,s,p,nums,index+1, result+1)
        else:
            if nums[index]//3+2 < p:
               # sys.stdout.write("cut\n")
                most = max(result, most)
            else:
                calc2(n,s,p,nums,index+1, result)

if __name__ == '__main__':
    main()
