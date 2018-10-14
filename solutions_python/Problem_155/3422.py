#!/usr/bin/python
# coding: utf-8

import sys
import os
import re
import datetime
import argparse


class Exo1Shyness(object):

    Tcase = 0
    filename = "A-small-attempt1.in"
    filenameout = "output.txt"
    def __init__(self):
        self.exosolution1()


    def exosolution1(self):
        print "Igotit"
        with open(self.filename, 'r') as f:
             read_data = f.readlines()
        f.closed

        with open(self.filenameout, 'w') as fileout:
            for index,row in enumerate(read_data):
                if index == 0 :
                    self.Tcase = row
                    print "Tcase:" + self.Tcase
                else:
                    if index > self.Tcase:
                        print "Erreur too big"
                    else:
                        self.parse_data(row, index, fileout)

    def parse_data(self, linetoparse, testcaseid, fileout):
        print linetoparse
        Smax = linetoparse.split(' ')[0]
        print "Smax:" + Smax
        linetodecode = linetoparse.split(' ')[1].strip()
        
        shynesslevel = 0
        neededperson = 0
        persontostand = 0
        for shyness in linetodecode:
            print shyness + " " + str(shynesslevel)
            if int(shyness) > 0:
                if persontostand < shynesslevel:
                    neededperson = neededperson + (int(shynesslevel) - persontostand)

                persontostand = int(shyness) + persontostand + neededperson
            print neededperson
            shynesslevel += 1

        stringtowrite = "Case #" + str(testcaseid) + ": " + str(neededperson) + "\n"

        fileout.write(stringtowrite)
        


### MAIN ###
if __name__ == "__main__":
	foo = Exo1Shyness()
