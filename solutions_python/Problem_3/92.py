import sys
from math import *

def areaBetweenChordAndCirle(r, arcAngle):
    subtendedArcArea = .5*arcAngle*r*r
    subtendedTriArea = .5*sin(arcAngle)*r*r

    return subtendedArcArea - subtendedTriArea

def areaFreeFourCornersIn(g, f):
    side = g - 2*f
    return side*side

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%f, %f)" % (self.x, self.y)

def areaOfRect(pt1, pt2):
    side1 = abs(pt1.x - pt2.x)
    side2 = abs(pt1.y - pt2.y)
    return side1*side2

def areaFreeThreeCornersIn(blPt, tIntersectPt, rIntersectPt, radius):
    overlapPt = Point(tIntersectPt.x, rIntersectPt.y)

    rectA = areaOfRect(blPt, tIntersectPt)
    rectB = areaOfRect(blPt, rIntersectPt)
    overlapRect = areaOfRect(blPt, overlapPt)
    rects = rectA + rectB - overlapRect

    return rects + areaFreeOneCornerIn(overlapPt, tIntersectPt, rIntersectPt, radius)

def areaFreeTwoCornersIn(blPt, tIntersectPt, bIntersectPt, radius):
    # hacklicious: assuming pt1 is on top
    
    triCorner = Point(tIntersectPt.x, bIntersectPt.y)

    return areaOfRect(blPt, tIntersectPt) + areaFreeOneCornerIn(triCorner, tIntersectPt, bIntersectPt, radius)

def areaFreeOneCornerIn(corner, tIntersectPt, rIntersectPt, radius):
    diffx = tIntersectPt.x - rIntersectPt.x
    diffy = tIntersectPt.y - rIntersectPt.y
    dist = sqrt(diffx*diffx + diffy*diffy)
    
    arcAngle = 2.0*asin(.5*dist/radius)

    triArea = .5*abs(diffx)*abs(diffy)
    chordArea = areaBetweenChordAndCirle(radius, arcAngle)

    return triArea + chordArea


def getFreeSquareCorners(i, j, r, g, f):
    xOffset = i*(2*r + g) + r + f
    yOffset = j*(2*r + g) + r + f

    side = g - 2*f

    corners = []
    corners.append(Point(xOffset, yOffset))
    corners.append(Point(xOffset, yOffset + side))
    corners.append(Point(xOffset + side, yOffset + side))
    corners.append(Point(xOffset + side, yOffset))

    return corners

def getCornersInside(corners, radius):
    inds = []
    for i, corner in enumerate(corners):
        if corner.x*corner.x + corner.y*corner.y <= radius*radius:
            inds.append(i)

    return inds

def probHit(f, R, t, r, g):
    safeRadius = R - t - f

    # We just do the top left quadrant and multiply by 4
    numGaps = int(ceil(safeRadius/(g + r)))

    freeArea = 0

    for i in range(numGaps):
        for j in range(numGaps):
            
            corners = getFreeSquareCorners(i, j, r, g, f)

            cornersInInds = getCornersInside(corners, safeRadius)
            numCornersIn = len(cornersInInds)    


            if numCornersIn == 4:
                freeArea += areaFreeFourCornersIn(g, f)
            elif numCornersIn == 3:
                tIntersectPt = Point(sqrt(safeRadius*safeRadius - corners[1].y*corners[1].y), corners[1].y)
                rIntersectPt = Point(corners[3].x, sqrt(safeRadius*safeRadius - corners[3].x*corners[3].x))
                freeArea += areaFreeThreeCornersIn(corners[0], tIntersectPt, rIntersectPt, safeRadius)
            elif numCornersIn == 2:
                # hacklicious use symmetry to skip half the cases
                if 1 in cornersInInds:
                    tIntersectPt = Point(sqrt(safeRadius*safeRadius - corners[1].y*corners[1].y), corners[1].y)
                    bIntersectPt = Point(sqrt(safeRadius*safeRadius - corners[3].y*corners[3].y), corners[3].y)
                    freeArea += 2*areaFreeTwoCornersIn(corners[0], tIntersectPt, bIntersectPt, safeRadius)
                else:
                    continue
            elif numCornersIn == 1:
                bIntersectPt = Point(sqrt(safeRadius*safeRadius - corners[0].y*corners[0].y), corners[0].y)
                lIntersectPt = Point(corners[0].x, sqrt(safeRadius*safeRadius - corners[0].x*corners[0].x))
                freeArea += areaFreeOneCornerIn(corners[0], lIntersectPt, bIntersectPt, safeRadius)

    return 1 - freeArea*4/(pi*R*R)

#print probHit(0.25, 1, 0.1, 0.01, .9)

inFile = sys.stdin
#inFile = open("input", 'r')

numCases = int(inFile.readline())
for caseNum in range(numCases):

    args = inFile.readline().split()
    params = [float(arg) for arg in args]
    
    pHit = probHit(*params)

    print "Case #%d: %f" % (caseNum + 1, pHit)


