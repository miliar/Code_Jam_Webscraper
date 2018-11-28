#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : parse.py
# Creation Date : 13-04-2013
# Last Modified : Sat 13 Apr 2013 10:49:27 AM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/


from sys import stdin

def readCase():
    case = []
    for i in range(4):
        case.append(stdin.readline().strip())
    stdin.readline()
    return case

def parse():
    T = int(stdin.readline())
    cases = []
    for i in range(T):
        cases.append(readCase())
    return cases

def main():
    pass
    

    
    

if __name__=="__main__":
    main()

