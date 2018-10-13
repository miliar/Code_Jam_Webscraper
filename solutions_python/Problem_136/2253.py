#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 Phiradet Bangcharoensap <phiradet@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def OptStrategy(C,F,X):
    cumTime = 0
    cookieRate = 2.0
    minTime = None
    while(True):
        ifEndNow = cumTime +  float(X)/float(cookieRate)
        #print float(X)/float(cookieRate), float(C)/float(cookieRate), ifEndNow
        if minTime == None:
            minTime = ifEndNow
        else:
            if minTime < ifEndNow:
                return minTime
            else:
                minTime = ifEndNow
        cumTime = cumTime + float(C)/float(cookieRate)
        cookieRate = cookieRate + F

def PrintAnswer(caseNum, time):
    print "Case #%d: %f"%(caseNum, time)

def main():
    tsNum = input()
    #print tsNum
    for currTs in range(tsNum):
        line = raw_input()
        #print line, currTs
        C,F,X = map(float, line.rstrip().split(' '))
        bestTime = OptStrategy(C,F,X)
        PrintAnswer(currTs+1, bestTime)
    return 0

if __name__ == '__main__':
    #print OptStrategy(500.0, 4.0, 2000.0)
	main()
