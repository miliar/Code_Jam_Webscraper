'''
Created on Apr 8, 2017

@author: conflict
'''

T = int(input())

for case in range(1, T+1):
    num = str(input())
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i+1]):
            firstApp = num.find(num[i])
            num = num[:firstApp] + str(int(num[i]) - 1) + '9' * (len(num)-(firstApp+1))
            break
    if num[0] == '0':
        num = num[1:]
    print("Case #{}: {}".format(case, num))
               
        
    