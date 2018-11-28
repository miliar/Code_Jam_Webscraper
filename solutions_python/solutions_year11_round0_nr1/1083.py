#!/usr/bin/env python
# encoding: utf-8
'''
Author: Almog Melamed
'''
import sys
import os
import itertools
import re


def main():
        ''' Empty file.out '''
        with open('small.out', mode='w', encoding='utf-8') as whocares:
                pass
        
        with open('small.in', encoding='utf-8') as jam:
                lineNumber = 0
                caseNumber = 0
                for line in jam:
                        lineNumber = lineNumber + 1

                        ''' Extract case number '''
                        if (lineNumber == 1):
                                continue
                        else:
                                caseNumber = lineNumber - 1

                        '''LOGIC'''
                        instructions = re.findall('[A-Za-z0-9]+', line)
                        numButtons = instructions[0]
                        allSteps = []
                        stepsB = []
                        stepsO = []
                        i = 1
                        while i < len(instructions):
                                allSteps.append(instructions[i])
                                if instructions[i] == 'O':
                                        stepsO.append(int(instructions[i+1]))
                                else:
                                        stepsB.append(int(instructions[i+1]))
                                
                                i += 2

                        stepsO.reverse()
                        stepsB.reverse()
                        allSteps.reverse()

                        '''calculating'''
                        numSeconds = 0
                        notDone = True
                        currPosB = 1
                        currPosO = 1
                        while notDone:
                                buttonPressed = False
                                if len(stepsO) > 0:
                                        if (currPosO == stepsO[-1]):
                                                if allSteps[-1] == 'O':
                                                        stepsO.pop()
                                                        allSteps.pop()
                                                        buttonPressed = True
                                        elif currPosO > stepsO[-1]:
                                                currPosO -= 1
                                        else:
                                                currPosO += 1
                                                
                                if len(stepsB) > 0:
                                        if (currPosB == stepsB[-1]):
                                                if allSteps[-1] == 'B' and (not buttonPressed):
                                                        stepsB.pop()
                                                        allSteps.pop()
                                        elif currPosB > stepsB[-1]:
                                                currPosB -= 1
                                        else:
                                                currPosB += 1


                                        
                                numSeconds += 1

                                if len(allSteps) == 0:
                                        notDone = False
                        
                        
                        
                        ''' Write answers to file '''
                        with open('small.out', mode='a', encoding='utf-8') as output:
                                output.write('Case #' + str(caseNumber) + ": " + str(numSeconds) + '\n')



if __name__ == '__main__':
	main()
