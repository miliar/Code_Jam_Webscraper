#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : parse.py
# Creation Date : 13-04-2013
# Last Modified : Sat 13 Apr 2013 02:50:39 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from sys import stdin

def readCase():
    return map(int, stdin.readline().split())

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

