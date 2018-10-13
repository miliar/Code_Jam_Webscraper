#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Andy
#
# Created:     11/04/2014
# Copyright:   (c) Andy 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division
def findothers(C,F,X):
    basespeed = X / 2
    farms = 0
    while True:
        farms += 1
        speed = 0
        for num_of_farms in range(farms):
            speed += C / (2 + (F * num_of_farms))
        speed += (X / (2+(F*farms)))

        if speed < basespeed:
            basespeed = speed
            speed = 0
        else :
            break
    return basespeed
def main():
    input_text = open("C:\Users\Andy\Downloads\B-small-attempt2.in")
    #input_text = open("test.txt")
    output_text = open("cookieclicker.txt","w")
    testcases = int(input_text.readline())
    testnum = 0
    while testnum < testcases:
        testnum += 1
        rawdata = input_text.readline()
        data = rawdata.split()
        C = float(data[0])
        F = float(data[1])
        X = float(data[2])
        speed = findothers(C,F,X)
        outstring = "Case #" + str(testnum) + ": " + str(speed) +"0000000"
        output_text.write(outstring)
        if not testnum == testcases:
            output_text.write("\n")


if __name__ == '__main__':
    main()
