#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
	friend_needed 	= 0
	stand_count		= 0
	max_shyness, aud_list = cipher.split()
	for index in xrange(0, int(max_shyness)+1):
		if int(aud_list[index]) > 0:
			if stand_count >= index:
				stand_count += int(aud_list[index])
			else:
				added_friend = index - stand_count
				stand_count  += added_friend + int(aud_list[index])
				friend_needed += added_friend

	return friend_needed


if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))