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
        flipper = int(row[1])
        signS = list(row[0].strip())
        flip = 0
        lenstring = len(signS)
        for i in range(0, lenstring - (flipper-1)):
            if signS[i] == '+':
                continue
            flip = flip + 1
            for j in range(i, i + flipper ):
                if signS[j] == '-':
                    signS[j] = '+'
                else:
                    signS[j] = '-'
        if '-' in signS:
            flip = 'IMPOSSIBLE' 
        stringtowrite = "Case #" + str(testcaseid) + ": " + str(flip) + "\n"
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
