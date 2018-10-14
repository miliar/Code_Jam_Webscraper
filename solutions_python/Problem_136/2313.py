#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 tusharmakkar08 <tusharmakkar08@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
	t=input()
	for kik in xrange(1,t+1):
		c,f,x=map(float,raw_input("").strip().split())
		kin=2
		nett=x/kin
		while 1:
			if (x*1.0/kin*1.0)<((x*1.0/(kin+f)*1.0)+(c*1.0/kin)):
				break
			nett=(((x*1.0/(kin+f)*1.0)+(c*1.0/kin))+(nett-(x*1.0/kin*1.0)))
			kin+=f
		print "Case #%r: %.10f"%(kik,nett)
	return 0

if __name__ == '__main__':
	main()

