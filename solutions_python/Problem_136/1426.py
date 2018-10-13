'''
Created on 12 Apr 2014
@author: Marin Georgiev
'''

with open("B-large.in", 'r') as f:
    t = int(f.readline())
    for i in range(t):
        test_case = "Case #"+str(i+1)+":"
        print test_case,
        nums = f.readline()[:-1].split(" ")
        C = float(nums[0])
        F = float(nums[1])
        X = float(nums[2])
        currCookies = 0
        currSpeed = 2
        time = 0
        while(currCookies<X):
            if((X-currCookies)*1.0/currSpeed > C*1.0/currSpeed + (X-currCookies)*1.0/(currSpeed+F)):
                time += C*1.0/currSpeed
                currSpeed += F
            else:
                time += (X-currCookies)*1.0/currSpeed
                currCookies += X-currCookies
        print time