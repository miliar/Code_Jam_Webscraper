#!/usr/bin/env python

import sys

dic = {}

def recit(a,c):
    if a not in dic:
        dic[a] = c

def rec_line(p,c):
    for k in range(len(p)):
        recit(p[k], c[k])

def init_dic():
    refs = open('refs.in', 'r')

    while True:
        plain = refs.readline()
        cipher = refs.readline()
        if not cipher: break
        rec_line(plain, cipher)

    refs.close()

def decod_line(line):
    s = ""
    for c in line:
        if c != '\n':
            s += dic[c]

    return s

init_dic()

p = int(sys.stdin.readline())
for s in range(1,p+1):
    line = sys.stdin.readline()
    print("Case #" + str(s) + ": " +  str(decod_line(line)))

