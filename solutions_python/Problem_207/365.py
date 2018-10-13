#!/usr/bin/python
# coding: utf-8

import sys
import os
import re
import datetime
import argparse


class Exo1(object):

    listcase = []
    Tcase = 0
    filename = "A-large.in"
    filenameout = "outputbig.txt"
    def __init__(self,args):
        self.filename = args['inputfilename']
        self.filenameout = args['outputfilename']
        self.exosolution1()


    def exosolution1(self):
        with open(self.filename, 'r') as f:
             read_data = f.readlines()

        with open(self.filenameout, 'w') as fileout:
            for index,row in enumerate(read_data):
                if index == 0 :
                    self.Tcase = row
                else:
                    if index > self.Tcase:
                        print "Erreur too big"
                    else:
                        self.parse_data(row, index, fileout)

    def parse_data(self, linetoparse, testcaseid, fileout):
        row = linetoparse.split()
        total = int(row[0])
        horse = row[1:]
        horseint = []
        color = ['R','O','Y','G','B','V']
        outputstr = ""
        index = -1
        for i,x in enumerate(horse):
            horseint.append(int(x))
        while True:
            b = {}
            for i,x in enumerate(horseint):
                if i!=index:
                    b[i] = int(x)
            prev = 0
            minindex = -1
            for j in b:
                if b[j] == prev and outputstr:
                    if color[j] == outputstr[0]:
                        minindex = j
                        prev = b[j]
                if b[j] > prev:
                    minindex = j
                    prev = b[j]
            if prev == 0:
                break
            horseint[minindex] = horseint[minindex] - 1
            outputstr = outputstr + color[minindex]
            index = minindex
        for i in horseint:
            if i != 0:
                outputstr = "IMPOSSIBLE"
                break
        if outputstr[0] == outputstr[len(outputstr)-1]:
            outputstr = "IMPOSSIBLE"
        print outputstr
        stringtowrite = "Case #" + str(testcaseid) + ": " + str(outputstr) + "\n"
        fileout.write(stringtowrite)

def initialize_args():
    parser = argparse.ArgumentParser(description='Nagios Sensor Status')
    parser.add_argument('-i', dest='inputfilename', help='Input Filename', required=True)
    parser.add_argument('-o', dest='outputfilename', help='Output Filename', required=True)
    parser.set_defaults(feature=False)
    args = vars(parser.parse_args())
    return args


### MAIN ###
if __name__ == "__main__":
    args = initialize_args()
    foo = Exo1(args)
