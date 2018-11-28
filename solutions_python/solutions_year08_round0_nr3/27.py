# Uses the euclid library by Alex Holkner (http://partiallydisassembled.net/euclid.html)
# with a little modification. The modified version is uploaded along with this source file.

import pprint
import math
import random
import psyco
from euclid import *

def sign(f):
    if f < 0:
        return -1
    elif f > 0:
        return 1
    else:
        return 0

def poly_area(points):
    a = 0
    for i in xrange(len(points)):
        i1 = (i+1) % len(points)
        a += points[i].x * points[i1].y - points[i1].x * points[i].y
    a /= 2.0
    return a

def angle_between_vecs(va, vb):
    rad_to_deg(math.acos(dot_prod(va, vb) / (vec_len(va) * vec_len(vb))))
   
def calc_circle_segment(p1, p2):
    v1 = Vector2(p1.x, p1.y)
    v2 = Vector2(p2.x, p2.y)

    l = v1.magnitude() * v2.magnitude()
    w = v1.dot(v2) / l
    if w >= 1.0:
        w = 1.0
    rad = math.acos(w)
    perc = rad / (2*math.pi)
    r = v1.magnitude()
    slice = r**2 * math.pi * perc

    a, b, c = v1.magnitude(), v2.magnitude(), p1.distance(p2)
    s = (a+b+c) / 2.0
    tri = math.sqrt(s * (s-a) * (s-b) * (s-c))

    return slice - tri

def box_isect_circle_area(box, r):
    c = Circle(Point2(0,0), r)
    nbox = []
    for i in xrange(4):
        i1 = (i+1) % 4
        l = LineSegment2(Point2(*box[i]), Point2(*box[i1]))
        li = c.intersect(l)
        if li:
            li = LineSegment2(li.p2, li.p1)
            nbox.append(li)

    poly = []
    for i in xrange(len(nbox)):
        i1 = (i+1) % 4
        p1 = nbox[i].p1
        p2 = nbox[i].p2
        poly.append(p1)
        poly.append(p2)

    tot = 0.0
    for i in xrange(len(poly)):
        i1 = (i+1) % len(poly)
        if i % 2 == 1 and (poly[i].x != poly[i1].x or poly[i].y != poly[i1].y):
            t = calc_circle_segment(poly[i], poly[i1])
            tot += t

    tot += math.fabs(poly_area(poly))
    return tot

psyco.full()

cases = int(raw_input())
for case in xrange(cases):
    f, R, t, r, g = [float(s) for s in raw_input().split()]

    res = 0.0
    if 2*f >= g:
        res = 1.0
    else:
        ri = R - t - f
        gg = g - 2*f

        K = int(math.ceil(R / (g + 2*r)))+1
        nohit = 0.0
        cache = {}
        for i in xrange(1, K+1):
            for j in xrange(1, K+1):
                cx = r + g / 2 + (i - 1) * (2 * r + g)
                cy = r + g / 2 + (j - 1) * (2 * r + g)

                box = []
                for dx, dy in ((-1,-1),(-1,1),(1,1),(1,-1)):
                    box.append((cx+dx*gg/2, cy+dy*gg/2))

                out = 0
                for p in box:
                    if math.hypot(p[0], p[1]) >= ri:
                        out += 1

                if out == 4:
                    nh = 0
                elif out > 0:
                    nh = box_isect_circle_area(box, ri)
                else:
                    nh = gg**2
                
                nohit += nh

        nohit *= 4

        hit = (R**2 - ri**2) * math.pi
        hit += ri**2 * math.pi - nohit
        area = R**2 * math.pi
        
        res = hit / area


    print 'Case #%d: %.6lf' % (case+1, res)

