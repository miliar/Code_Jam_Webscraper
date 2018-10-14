from __future__ import division
from math import pi, sqrt, sin, asin

def read_file(filepath):
    try:
        lines = file(filepath, 'rU').readlines()
    except IOError, e:
        print '*** file open failed:', filepath
        raise e
    else:
        return lines

def get_box(x, y):
    # x0,y1    x1,y1
    #
    # x0,y0    x1,y0
    x0 = r + (g+2*r)*x + f
    x1 = x0 + g - 2*f
    y0 = r + (g+2*r)*y + f
    y1 = y0 + g - 2*f
    return x0, y0, x1, y1

def get_area(from_x, to_x):
    from_theta = asin(from_x/a)
    to_theta = asin(to_x/a)
    arc_area = (to_theta-from_theta)/2 + (sin(2*to_theta)-sin(2*from_theta))/4
    arc_area *= a*a
    return arc_area
    
# main
lines = read_file('./C-small-attempt0.in')
for i in range(len(lines)):
    lines[i] = lines[i].rstrip('\r\n')
print lines

N = int(lines[0])
answers = []
i = 1
for n in range(N):
    # read a case
    print 'case #'+str(n+1)+':'
    f, R, t, r, g = lines[i].split(' ')
    i += 1
    f = float(f)
    R = float(R)
    t = float(t)
    r = float(r)
    g = float(g)
    a = R-t-f
    print 'f:', f, 'R:', R, 't:', t, 'r:', r, 'g:', g, 'a:', a
    
    # check for 0
    if g-2*f<=0:
        answers.append(1)
        continue
    
    # diagonal boxes
    diagonal_area = 0
    nondiagonal_area = 0
    x = 0
    y = 0
    while(True):
        x0, y0, x1, y1 = get_box(x, y)
        # outside
        if x0*x0+y0*y0>=a*a:
            if x==y:
                print 'diagonal outside:', x
                break
            else:
                print 'non-diagonal outside:', x, y
                y += 1
                x = y
                continue
        
        print 'x:', x, 'y:', y, 'x0:', x0, 'y0:', y0, 'x1:', x1, 'y1:', y1
        
        area = 0
        # for diagonal
        if x==y:
            # cross at far
            if (x0*x0+y1*y1-a*a)*(x1*x1+y1*y1-a*a)<=0:
                x2 = sqrt(a*a-y1*y1)
                area = (x2-x0)*(y1-y0) + get_area(x2, x1) - (x1-x2)*y0
                print 'far', area, 'x2:', x2
            # cross at near
            elif (x0*x0+y0*y0-a*a)*(x1*x1+y0*y0-a*a)<=0:
                x2 = sqrt(a*a-y0*y0)
                area = get_area(x0, x2) - (x2-x0)*y0
                print 'near', area, 'x2:', x2
            # no cross
            else:
                area = (g-2*f)*(g-2*f)
                print 'no_cross', area
            diagonal_area += area
            x += 1
        # for non-diagonal
        else:
            # cross at top
            if (x0*x0+y1*y1-a*a)*(x1*x1+y1*y1-a*a)<=0:
                x2 = sqrt(a*a-y1*y1)
                # top & right
                if (x1*x1+y0*y0-a*a)*(x1*x1+y1*y1-a*a)<=0:
                    #y2 = sqrt(a*a-x1*x1)
                    area = (x2-x0)*(y1-y0) + get_area(x2, x1) - (x1-x2)*y0
                    print 'top & right', area
                # top & bottom
                elif (x0*x0+y0*y0-a*a)*(x1*x1+y0*y0-a*a)<=0:
                    x3 = sqrt(a*a-y0*y0)
                    area = (x2-x0)*(y1-y0) + get_area(x2, x3) - (x3-x2)*y0
                    print 'top & bottom', area
                # top & ?
                else:
                    print 'top & ?'
                    exit(1)
            # cross at left
            elif (x0*x0+y0*y0-a*a)*(x0*x0+y1*y1-a*a)<=0:
                y2 = sqrt(a*a-x0*x0)
                # left & right
                if (x1*x1+y0*y0-a*a)*(x1*x1+y1*y1-a*a)<=0:
                    #y3 = sqrt(a*a-x1*x1)
                    area = get_area(x0, x1) - (x1-x0)*y0
                    print 'left & right', area
                # left & bottom
                elif (x0*x0+y0*y0-a*a)*(x1*x1+y0*y0-a*a)<=0:
                    x2 = sqrt(a*a-y0*y0)
                    area = get_area(x0, x2) - (x2-x0)*y0
                    print 'left & bottom', area
                # left & ?
                else:
                    print 'left & ?'
                    exit(1)
            # no cross
            else:
                area = (g-2*f)*(g-2*f)
                print 'no_cross', area
            nondiagonal_area += area
            x += 1
                        
    ok_area = (diagonal_area + nondiagonal_area*2)*4
    total_area = pi*R*R
    p = 1 - ok_area/total_area
    answers.append(p)
    print 'ok_area:', ok_area, 'total_area:', total_area, 'p:', p
    
# answers
for n in range(N):
    print 'Case #'+str(n+1)+': %1.6f' % answers[n]

