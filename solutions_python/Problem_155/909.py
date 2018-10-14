#!/usr/bin/env python
# -*- coding: utf-8 -*-
def solve(data):
	i = res = standing_people = 0
	standing_people = int(data[0])
	for value in data[1:]:		
		#print i, standing_people
		people_needed = 0
		if standing_people <=  i and value != '0':
			people_needed = i - standing_people + 1
			res += people_needed
		i += 1
		#print res, standing_people
		standing_people += (int(value) + people_needed)
		
	return res
	
if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        data = raw_input()
        print("Case #%i: %s" % (caseNr, solve(data.split(" ")[1])))

