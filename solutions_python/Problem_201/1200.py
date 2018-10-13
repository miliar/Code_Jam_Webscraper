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
        seats = int(row[0])
        persons = int(row[1].strip())

        seats = float(int(seats) / 2.0)
#        persons,personsmodul = divmod(int(persons), 2.0)
        personsmodul = int(persons) /2
        persons = float(int(persons)/2.0)
        personsmodul = float(persons - personsmodul)
        while persons >= 1.0:
            seats = seats - personsmodul
            #persons,personsmodul = divmod(int(persons), 2.0)
            personsmodul = int(persons) /2
            persons = float(int(persons)/2.0)
            personsmodul = float(persons - personsmodul)
            seats = float(int(seats) / 2.0)

        minseats = int(seats - persons)
        maxseats = int(seats)
        output = "%s %s" % (maxseats,minseats)
        stringtowrite = "Case #" + str(testcaseid) + ": " + str(output) + "\n"
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
