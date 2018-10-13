#!/usr/bin/env python
# encoding: utf-8
"""
script.py

Created by Vladimir Prudnikov on 2008-07-17.
Copyright (c) 2008 Prudnikov Vladimir. All rights reserved.

Made on 
"""

import sys
import os
import math



def main():
	
	input_filename = sys.argv[1]
	
	f = open(input_filename)
	count = int(f.readline().strip())
	
	case = 1
	
	
	for i in xrange(count):
		T = int(f.readline().strip())
		NA, NB = f.readline().strip().split(" ")
		NA = int(NA)
		NB = int(NB)
		
		atrains = []
		btrains = []
		
		for i in xrange(NA):
			ta, tb = f.readline().strip().split(" ")
			ta = int(ta.split(":")[0])*60 + int(ta.split(":")[1])
			tb = int(tb.split(":")[0])*60 + int(tb.split(":")[1])
			atrains.append([ta, tb])
		
		
		for i in xrange(NB):
			tb, ta = f.readline().strip().split(" ")
			ta = int(ta.split(":")[0])*60 + int(ta.split(":")[1])
			tb = int(tb.split(":")[0])*60 + int(tb.split(":")[1])
			btrains.append([tb, ta])
		

		def trains_count(out_trains, in_trains, T):
			trains_ready = [t[1]+T for t in in_trains]
			trains_out = [t[0] for t in out_trains]


			trains = 0
			waiting = 0

			if len(out_trains)>0:
				for i in xrange(1440):
					time = i
					
					if time in trains_ready:
						waiting = waiting + trains_ready.count(time)
					
					if time in trains_out:
						out_count = trains_out.count(time)
						if waiting >= out_count:
							waiting = waiting - out_count
						elif waiting > 0:
							trains = trains + out_count - waiting
							waiting = 0
						else:
							trains = trains + out_count
			return trains
		
		a = trains_count(atrains, btrains, T)
		b = trains_count(btrains, atrains, T)
		
		print "Case #%s: %s %s" % (case, a, b)
		case = case + 1
	
	f.close()

	
if __name__ == '__main__':
	main()

