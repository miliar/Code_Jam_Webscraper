#!/usr/bin/env python
# encoding: utf-8
'''Author: Almog Melamed'''
import sys
import os
import re
import itertools


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
                                caseNumber = caseNumber + 1
                        
                        '''LOGIC'''
                        rules = re.findall('[0-9A-Za-z]+', line)

                        instructions = rules[-1]

                        '''@Refactor: doesn't work for big test'''
                        if rules[0] != '0':
                                combo = rules[1]
                                if rules[2] != '0':
                                        oppose = rules[3]
                                else:
                                        oppose = None
                        else:
                                combo = None
                                if rules[1] != '0':
                                        oppose = rules[2]
                                else:
                                        oppose = None

                        '''parse instructions'''
                        queue = ''
                        for i in instructions:
                                queue = queue + i;

                                '''combo?'''
                                if combo != None:
                                        if len(queue) > 1 and ((queue[-1] == combo[0] and queue[-2] == combo[1]) or (queue[-1] == combo[1] and queue[-2] == combo[0])):
                                                queue = queue[0:-2] + combo[2]

                                '''opposes?'''
                                if oppose != None:
                                        if oppose[0] == queue[-1]:
                                                if queue.find(oppose[1]) != -1:
                                                        queue = ''
                                        elif oppose[1] == queue[-1]:
                                                if queue.find(oppose[0]) != -1:
                                                        queue = ''

                        ''' Write answers to file '''
                        with open('small.out', mode='a', encoding='utf-8') as output:
                                happyEnding = 'Case #' + str(caseNumber) + ": ["
                                for instruction in queue:
                                        happyEnding += instruction + ", "
                                happyEnding = happyEnding.rstrip(', ')
                                happyEnding += ']\n'
                                output.write(happyEnding)


if __name__ == '__main__':
	main()
