'''
Created on Apr 13, 2013

@author: Allen
'''

import os

def canMow(arr):
    # find max element
    width, height = [], []
    for i in range(len(arr)):
        height.append(max(arr[i]))
    for i in range(len(arr[0])):
        width.append(max([row[i] for row in arr]))
    
    mowable = []
    for i in range(len(arr)):
        curr = []
        for j in range(len(arr[0])):
            curr.append(min([width[j], height[i]]))
        mowable.append(curr)
    
    if mowable==arr:
        return 'YES'
    else:
        return 'NO'

if __name__=="__main__":
    ext = 'large'
    cases = []
    with open(os.path.join(os.path.dirname(__file__), 'B-' + ext + '.in')) as f:
        number = int(f.readline())
        for dummy in range(number):
            size = [int(i) for i in f.readline().split()]
            curr = []
            for row in range(size[0]):
                curr.append([int(i) for i in f.readline().split()])
            cases.append(curr)
    
    output = ""
    for i in range(number):
        output += "Case #{0}: {1}\n".format(i+1, canMow(cases[i]))
    
    with open(os.path.join(os.path.dirname(__file__), 'B-' + ext + '.out'), 'w') as f:
        f.write(output[:-1])