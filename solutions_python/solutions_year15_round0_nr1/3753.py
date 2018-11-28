#!/usr/bin/env python
# -*- coding: utf-8 -*-




def main():
	

	fRead()
	
	return 0
	
def fRead():
	fo = open("p1input","r")
	ffo = open("P1Output","wb")
	cases = fo.readline()
	
	for i in range(int(cases)):
		
		tmpstr = fo.readline()
		if tmpstr =="":
			break
		tmpAudienceArray = list(tmpstr)
		tmpAudienceArray.pop()
		tmpAudienceArray.reverse()
		tmpAudienceArray.pop()
		tmpAudienceArray.pop()
		tmpAudienceArray.reverse()
			
		audienceArray = tmpAudienceArray
		ffo.write( "Case #" +  str(i+1) + ": " + minFriends(audienceArray)+"\n")
	ffo.close()
	fo.close()
	
def minFriends(audience):
	i=0
	curMembers=0
	friends=0
	
	for members in [int(a) for a in audience]:

		if curMembers<i:
			friends=friends+1
			curMembers=curMembers+1
		curMembers=curMembers+members
		i=i+1
	return str(friends)
		
		
if __name__ == '__main__':
	main()

