#!/usr/bin/env python

import sys
import struct
import ctypes


def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))




T = int(sys.stdin.readline())

for case in range(0, T):
	part = sys.stdin.readline()
        up, down = part.split("/")
 
        up = int(up)
        down = int(down)

        if int(bin(up&down)[2:]) != 0:
                print "Case #%s: impossible" % (str(case+1) )
        else:
                for i in range(1, 40):
                        up = 2*up
                        if up >= down:
                                print "Case #%s: %d" % (str(case+1), i )
                                break
