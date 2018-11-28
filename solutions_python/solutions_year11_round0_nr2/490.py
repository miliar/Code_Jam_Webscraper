#!/usr/bin/env python
# encoding: utf-8
"""
problemB.py

Created by Joshua Olson on 2011-05-05.
Copyright (c) 2011 solarmist. All rights reserved.
"""

import sys
import os


def main():
    data = sys.stdin.readlines()
    cases = int(data.pop(0))
    for case in range(cases): #line is an int containing the index of the case
        print 'Case #' + str(case + 1) + ':',
        caseData = data.pop(0).split()
        
        #Base letters can be Q, W, E, R, A, S, D, F
        combinations = {}
        numComb = int(caseData.pop(0))
        for i in range(numComb):
            item = caseData.pop(0)
            combinations[item[:2]] = item[-1:] #Backwards and forwards
            combinations[item[:2][::-1]] = item[-1:]
            
        cancel = {}
        numCancel = int(caseData.pop(0))
        for i in range(numCancel):
            item = caseData.pop(0)
            cancel[item] = list(item)
            
        elements = []
        numEle = int(caseData.pop(0))
        item = ''
        el = list(caseData.pop(0))
        for i in range(numEle):
            #First check for combinations in the first i elements
            i = len(elements)
            elements.append(el.pop(0))
            if i > 0:
                combo = elements[i-1] + elements[i]
                
                if combo in combinations.keys():
                    elements.pop() #drop the last element and replace it
                    elements[i - 1] = combinations[combo]
                    i -= 1
                    
                for key in cancel.keys():
                    if cancel[key][0] in elements and cancel[key][1] in elements:
                        elements = []
                            
        print '[' +', '.join(elements) + ']'
         
if __name__ == '__main__':
	main()

