#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

def main(argv=None):
    if len(argv)<1:
        print "Please specify input file"
        return 1
    fh = open(argv[0], 'rt')
    line = fh.readline().strip()
    T = int(line)
    for i in range(T):
        size=fh.readline().strip().split(" ")
        row=int(size[0])
        column=int(size[1])
#        print "row %d column %d"%(row,column)
        lawn=[]
        heights=[]
        for j in range(row):
            tmp=fh.readline().strip().split(" ")
            tmplist=[]
            for num in tmp:
                tmplist.append(int(num))
                if not int(num) in heights:
                    heights.append(int(num))
            lawn.append(tmplist)
        heights.sort(reverse=True)
        del heights[0]
#        print "lawn %s"%str(lawn)
#        print "heights %s"%str(heights)
	check_case(i, lawn, row, column, heights)
    fh.close()

def check_case(i, lawn, row, column, heights):
    # examine lawn
    for j in heights:
        doable_rows=[]
        doable_columns=[]
	for k in range(row):
	    workable=True
	    for l in range(column):
		if lawn[k][l]>j:
		    workable=False
		    break
	    if workable:
	        doable_rows.append(k)
        for k in range(column):
	    workable=True
            for l in range(row):
                if lawn[l][k]>j:
		    workable=False
                    break
	    if workable:
                doable_columns.append(k)
#	print "rows %s"%str(doable_rows)
#	print "cloumns %s"%str(doable_columns)
        for k in range(row):
            for l in range(column):
               if lawn[k][l]==j and (not k in doable_rows and not l in doable_columns):
                    print "Case #%d: NO"%(i+1)
		    return 
    print "Case #%d: YES"%(i+1)




if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

