#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os.path
import numpy as np

def search( TestStringPosition, LinePosition):
    global TestStringLen, Answer, Start, Line, TestString
    if TestStringPosition > TestStringLen-1:
        Answer += 1
        if Answer > 9999:
            Answer %= 10000
    else:
        while LinePosition <= End-TestStringLen+TestStringPosition+1:
            if Line[LinePosition] == TestString[TestStringPosition]:
                search( TestStringPosition+1, LinePosition + 1)
            LinePosition += 1
 
            
# Входной файл
if len(sys.argv) < 2:
    #sInputFileName = 'C-small-attempt0.in'
    sInputFileName = 'c.in'
    #sys.exit()
else:
    sInputFileName = sys.argv[1]
print sInputFileName

# Выходной файл
sOutputFileName = os.path.splitext( sInputFileName )[0]+'.out'
print sOutputFileName

InDataFile = open( sInputFileName )
OutDataFile = open( sOutputFileName, 'wt' )
TestString = 'welcome to code jam'
TestStringLen = len(TestString)

NumCases = int(InDataFile.readline().rstrip())
for case in range(NumCases):
    Line = InDataFile.readline().rstrip()
    Answer = 0
    Start = Line.find('w')
    End = Line.rfind('m')
    if (End > Start) and (End !=-1) and (Start != -1) and \
       ((End-Start+1) >= TestStringLen):
        # проверяем на количество символов
        for x in TestString:
            pass
        # ищем в промежутке Start:End+1
        CurTestStringPosition = 0
        CurLinePosition = Start
        while CurLinePosition <= End-TestStringLen+1:
            if Line[CurLinePosition] == TestString[CurTestStringPosition]:
                search( CurTestStringPosition+1, CurLinePosition + 1)
            CurLinePosition += 1
    print 'Case #%d: %04d' % (case+1, Answer)
    OutDataFile.write('Case #%d: %04d\n' % (case+1, Answer))
OutDataFile.close()    
InDataFile.close()

