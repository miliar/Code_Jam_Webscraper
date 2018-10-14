#!/usr/bin/python

import re
import sys

input_file = open('C-large.in')
output_file = open('C-large.out', 'w')

T = int(input_file.readline())

cache = {}
def get_recycleds(n):
    global cache
    if n in cache:
        return cache[n]
    
    if n < 21:
        cache[n] = []
        return []
    
    l = 1
    d = 10
    while d < n:
        d *= 10
        l+=1
    
    g = 1
    d = 10
    result = []
    while d < n:
        m = n%d
        if m >= d/10:
            s = m * 10**(l-g) + n/d
            if s != n: 
                result.append(s)
        d *= 10
        g += 1

    cache[n] = result
    return result

for t in range(T):
    A, B = map(int, input_file.readline().split(' '))

    result = 0
    used = set()
  
    for i in range(A, B+1):
        recycleds = get_recycleds(i)
        for recycled in recycleds:
            if recycled >= A and recycled <= B and not (i, recycled) in used:
                used.add((i, recycled))
                used.add((recycled, i))
                result += 1
    
  
    output_file.write("Case #" + str(t + 1) + ": " + str(result) + "\n")
        

input_file.close()
output_file.close()
