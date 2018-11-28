import re
import numpy

def Output(CaseN, res):
    Status = "YES" if res else "NO"
    outputLine = "Case #"+str(CaseN)+": "+Status
    fw.write(outputLine + "\n")

def ReadExample(N, M):
    Example = []
    for i in xrange(N):
        Example.append( map ( lambda x: int(x), lines.pop(0).split(' ') ) )
    return Example

def FindMax(Field, Fixed):
    NewField = Field[:]
    for i in xrange( len(Field) ):
        for j in xrange( len(Field[i]) ):
            NewField[i][j] = Field[i][j] - Fixed[i][j]
    #print Fixed
    #exit()
    return numpy.unravel_index( numpy.argmax(NewField), numpy.shape(NewField) ) #### NUMPY RULLLLSSS


def CheckVerticalCut(Fixed, cj, CutValue):
    FixedLine = map ( lambda l: l[cj], Fixed)
    return CheckCut(FixedLine, CutValue)


def CheckHorizontalCut(Fixed, ci, CutValue):
    return CheckCut(Fixed[ci], CutValue)

def CheckCut(FixedLine, CutValue):
    matches = [x for x in FixedLine if x > CutValue]
    return len(matches) == 0

def HorizontalCut(Current, ci, CutValue):
    NewCurrent = Current[:]
    NewCurrent[ci] = map (lambda CurrentValue: min(CurrentValue, CutValue) , Current[ci])
    return NewCurrent

def VerticalCut(Current, cj, CutValue):
    NewCurrent = Current[:]
    #print "NC", NewCurrent, cj
    for ci in xrange( len(NewCurrent) ):
        NewCurrent[ci][cj] = min(Current[ci][cj], CutValue)
    return NewCurrent

def CutMax(Example, Current, Fixed):
    (mi, mj) = FindMax(Example, Fixed)
    # test cuts
    MaxValue = Example[mi][mj]
    #print mi, mj, MaxValue
    if MaxValue == 0:
        return True

    if ( CheckHorizontalCut(Fixed, mi, MaxValue) ):
        NewCurrent = HorizontalCut(Current, mi, MaxValue)
        NewFixed = Fixed[:]
        NewFixed[mi][mj] = MaxValue
        #print "Newfixed Hor", NewFixed
        if CutMax(Example, NewCurrent, NewFixed):
            return True

    if ( CheckVerticalCut(Fixed, mj, MaxValue) ):
        NewCurrent = VerticalCut(Current, mj, MaxValue)
        NewFixed = Fixed[:]
        NewFixed[mi][mj] = MaxValue
        #print "Newfixed ver", NewFixed
        if CutMax(Example, NewCurrent, NewFixed):
            return True


    return False # False
##################################

#f = open('B-small-practice.in', 'r')
f = open('B-small.in', 'r')
#f = open('B-large.in', 'r')
fw = open('B.out', 'w')
lines = f.readlines()
T = int( lines.pop(0) )

for i in xrange(T):
    N, M = map ( lambda x: int(x), lines.pop(0).split(' ') )
    Example = ReadExample(N, M)
    Current = [[100 for k in xrange(M)] for l in xrange(N)]
    Fixed = [[0 for k in xrange(M)] for l in xrange(N)]
    res = CutMax(Example, Current, Fixed)
    Output(i+1, res)