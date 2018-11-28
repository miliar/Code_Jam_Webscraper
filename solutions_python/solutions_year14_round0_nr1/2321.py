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

def GetRow(n):
    ans = []
    for i in range(4):
        line = raw_input().rstrip()
	if i==n-1:
	    lineSpl = line.split(' ')
	    ans = map(int, lineSpl)
    return ans

def PrintAnswer(caseNum, answer):
    ansStr = ''
    if len(answer)==1:
	ansStr = str(answer.pop())
    elif len(answer)==0:
	ansStr = "Volunteer cheated!"
    else:
	ansStr = "Bad magician!"
    print "Case #%d: %s"%(caseNum, ansStr)

def main():
    allCaseNum = input()
    for caseNum in range(allCaseNum):
	rowNum = input()
	selectedRow1 = GetRow(rowNum)
	rowNum = input()
	selectedRow2 = GetRow(rowNum)
	answer = set(selectedRow1).intersection(set(selectedRow2))
	PrintAnswer(caseNum+1, answer)
    return 0

if __name__ == '__main__':
	main()

