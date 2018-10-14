
import re
from math import sin, cos, acos
file = open("C-large.in")
n = int(file.readline())
ans = open("1.out","wt")
pi = 3.14159265348979323846264338


def are_in_circle(points, R):
    #checks if all the points of a polygon (square too) are inside a circle
    #with center at (0,0) and radius R
    ans = [ ((point[0]**2 + point[1]**2) <= R**2) for point in points]
    ans = reduce(lambda a,b: a&b, ans)
    return ans
    
def cross(la,lb):
    return [ [a,b] for a in la for b in lb]

def get_points_from_rect(x,y):
    return[
            (x + f,     y + f),
            (x + f,     y - f + g),
            (x - f + g, y + f),
            (x - f + g, y - f + g),
    ]


def calculate_shitty_rectangles(shitty_rectangles):
    R1 = R - f - t
    total_area = 0.0
    for rect in shitty_rectangles:
        x,y = rect
        points = get_points_from_rect(x,y)
        collisions = []
        try:
            col = (R1*R1 - points[0][0]*points[0][0])**0.5
            if col >= points[0][1] and col <= points[1][1]:
                collisions.append([points[0][0],col])
        except:
            pass
        try:
            col = (R1*R1 - points[1][1]*points[1][1])**0.5
            if col >= points[1][0] and col <= points[3][0]:
                collisions.append([col,points[1][1]])
        except:
            pass    
        try:
            col = (R1*R1 - points[2][0]*points[2][0])**0.5
            if col >= points[2][1] and col <= points[3][1]:
                collisions.append([points[2][0],col])
        except:
            pass
        try:
            col = (R1*R1 - points[0][1]*points[0][1])**0.5
            if col >= points[0][0] and col <= points[2][0]:
                collisions.append([col,points[0][1]])
        except:
            pass
        #print collisions
        #at this point there will be either two or zero collisions
        #basically, it should always go here
        if len(collisions) == 2:
            area = 0
            #area under the arc
            x0 = min(collisions[0][0], collisions[1][0])
            x1 = points[2][0]
            y0 = points[0][1]
            y1 = min(collisions[0][1], collisions[1][1])
            #print "Rectangle: (%f %f) (%f %f)"%(x0,y0,x1,y1)
            area = max(0, (x1-x0)*(y1-y0)) #the max is redundant
            #print area
            total_area += area
            #area to the left of the arc
            x0 = points[0][0]
            x1 = min(collisions[0][0], collisions[1][0])
            y0 = min(collisions[0][1], collisions[1][1])
            y1 = points[1][1]
            #print "Rectangle: (%f %f) (%f %f)"%(x0,y0,x1,y1)
            area = max(0, (x1-x0)*(y1-y0)) #the max is redundant
            #print area
            total_area += area
            #area to the down-left of the arc
            x0 = points[0][0]
            x1 = min(collisions[0][0], collisions[1][0])
            y0 = points[0][1]
            y1 = min(collisions[0][1], collisions[1][1])
            #print "Rectangle: (%f %f) (%f %f)"%(x0,y0,x1,y1)
            area = max(0, (x1-x0)*(y1-y0)) #the max is redundant
            #print area
            total_area += area
            
            #area of the arc
            a = min(collisions[0][0], collisions[1][0])
            b = max(collisions[0][0], collisions[1][0])
            c = min(collisions[0][1], collisions[1][1])
            theta1 = acos(a/R1)
            theta2 = acos(b/R1)
            areaa = R1*R1/4 * (2*theta1 - sin(2*theta1))
            areab = R1*R1/4 * (2*theta2 - sin(2*theta2))
            area = areaa - areab - c*(b-a)
            #After many many tries I got the correct formula!!!

            #print area
#            print collisions[0][1], collisions[1][1]
#            print 2*R1*R1/pi*sin(b*pi/(2*R1)), 2*R1*R1/pi*sin(a*pi/(2*R1))
#            area = 2*R1*R1/pi * ( (sin(b*pi/(2*R1)) - sin(a*pi/(2*R1)))) - c*(b-a)
            
            """
            print "a: %f, b: %f, c: %f, R1: %f, area: %f"%( a,b,c,R1,area)
            print 2*R1/pi
            print (sin(b*pi/(2*R1)))
            print (sin(a*pi/(2*R1)))
            print -1*c*(b-a)
            """
            total_area += area
            
    print "Total area from shitty rectangles: %f"% total_area
    return total_area
        


for z in range(0,n):
    line = re.sub("\n|\r", "", file.readline())
    f, R, t, r, g = [float(item) for item in line.split(" ")]
    #print f, R, t, r, g
    area = float(0)
    area_normal = (g - 2*f) * (g - 2*f)
    shitty_rectangles = []
    print "Normal area of rectangle is: %f" % area_normal
    if 2*f >= g:
        ans.write("Case #%d: %f\n"%(z+1, 1.0))
        print "Case #%d: %f"%(z+1, 1.0)
    else:
        #get lines coordinates
        coords = []
        now = r
        while now < R - t - f:
            #Get only the lower left corners
            coords.append(now)
            now += g + 2*r
            
        #print coords
        rects = cross(coords,coords)
        #print rects
        for rect in rects:
            x = rect[0]
            y = rect[1]
            points = get_points_from_rect(x,y)
            if are_in_circle(points, R - t - f):
                area += area_normal
            else:
                shitty_rectangles.append(rect)
            #print points
        
        shitty_rectangles_area = calculate_shitty_rectangles(shitty_rectangles)
        area += shitty_rectangles_area
        area_circle = pi*R*R/4
        print "Squares Area = %f" % area
        print "Circle Area = %f" % area_circle
        probability = (area_circle - area) / area_circle
        print "Case #%d: %f" % (z+1, probability)
        ans.write("Case #%d: %f\n" % (z+1, probability))
