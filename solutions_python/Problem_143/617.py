'''
Created on May 3, 2014

@author: Andrew
'''
def solve(a,b,k):
    counter = 0 
    for num in range(0,a):
        for numb in range(0,b):
            if num & numb < k:
                counter += 1
    return counter

with open("google.in", "r") as infile, open("solution.txt", "w") as outfile:
    cases = int(infile.readline())
    for case in range(0,cases):
        a = infile.readline().split()
        b = solve(int(a[0]),int(a[1]),int(a[2]))
        outfile.write("Case #" + str(case+1) + ": " + str(b) + "\n")
        