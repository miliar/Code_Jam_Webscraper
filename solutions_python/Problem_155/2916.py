from __future__ import print_function
import sys

x = 0;
n = sys.stdin.readline()
n = int(n)

while (x < n):
    x = x + 1 #count
    num = 0
    friends = 0
    standing = 0
  
    r = sys.stdin.readline()
	
    people = []
    people = r.split()
    num = int(people[0])
    
    for i in range(num + 1):
        if friends + standing < i:
            friends = friends + (i - friends - standing)
        standing = standing + int(people[1][i])
 
    print("Case #",x,": ",friends, sep='')
    
    
    