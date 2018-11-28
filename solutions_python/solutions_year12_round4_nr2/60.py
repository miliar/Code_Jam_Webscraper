# -*- coding: utf-8 -*-
# <nbformat>3</nbformat>

# <codecell>

def readline_ints():
    return [int(num) for num in fin.readline().strip().split()]

# <codecell>

class Student:
    def __init__(self, i, reach):
        self.i = i
        self.reach = reach

# <codecell>

def update_corners(corners, x0, y0, x1, y1):
    newcorners = deque()
    for x,y in corners:
        if (y < y1) and (x < x0):
            y = y1
        elif (x < x1) and (y < y0):
            x = x1
        newcorners.append((x, y))
    return newcorners

# <codecell>

from collections import deque

# Update this with the filename
fname = "B-small-attempt1"
with open(fname+".in","r") as fin, open(fname+".out","w") as fout:

    numcases = readline_ints()[0]
    print(numcases, "cases")
    
    for caseno in range(1, numcases+1):
        # Code goes here
        N, W, L = readline_ints()
        students = [Student(i, reach) for i, reach in enumerate(readline_ints())]
        students.sort(key=lambda s: s.reach, reverse=True)
        free_corners = deque([(0,0)])
        for student in students:
            reach = student.reach
            x, y = free_corners.popleft()
            while (x != 0 and (W-x < reach)) \
                or (y != 0 and (L-y < reach)):
                free_corners.append((x,y))
                x, y = free_corners.popleft()
            
            centreX = 0 if x==0 else x+reach
            centreY = 0 if y==0 else y+reach
            student.locn = (centreX, centreY)
            farX = centreX+reach
            farY = centreY+reach
            if farX < W:
                free_corners.appendleft((farX, y))
            if farY < L:
                free_corners.append((x, farY))
            
            free_corners = update_corners(free_corners, x, y, farX, farY)
        
        students.sort(key=lambda s: s.i)
        result = " ".join("%d %d" % s.locn for s in students)
        
        outstr = "Case #%d: %s" % (caseno, result)
        fout.write(outstr + "\n")
        print(outstr)

# <codecell>


