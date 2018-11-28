import sys
import getopt
import re

ALPHA = "abcdefghijklmnopqrstuvwxyz"
forward = {}
backward = {}

def process(nums):
    N=nums[0]
    S=nums[1]
    p=nums[2]
    numbers = nums[3:]

    winners = 0 ## not surprising # of winners
    surprising_winners = 0

    for totscore in numbers:
        if p == 0:
            winners += 1
            continue
        if totscore < 3*p-4 or totscore < p:
            continue
        if totscore >= 3*p-2:
            winners += 1   ## not surprising
        else:
            surprising_winners += 1


    return winners + min(surprising_winners,S)

if __name__ == "__main__":

    #f= open('temp.in','r')
    f = open('B-large.in','r')
    f.readline()
    i = 0
    for line in f:
        i = i+1
        pr = "Case #"
        pr += str(i)
        pr += ": "
        
        nums = [int(x) for x in line.split()]
        
        pr += str(process(nums))
        print pr


    


