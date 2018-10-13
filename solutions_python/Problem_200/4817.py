import cgi, cgitb, sys, os
import requests
import urllib, urllib3
from bs4 import BeautifulSoup, SoupStrainer
import types
import re
import unicodedata
from operator import itemgetter
import codecs
from lxml import etree
import shutil


handle = open("C:/Users/Admin/Downloads/B-small-attempt1.in", "r")
conts = handle.read().split("\n")
handle.close()
outhandle = open("C:/Users/Admin/Downloads/B-small-attempt1.out","w")
#conts = [1, "1345"]
T = int(conts[0])
for i in range(0,T):
	curnum = list(conts[i+1])
	curnum = map(int, curnum)
	# find the junction point
	numlen = len(curnum)
	junctionPoint = -1
	for k in range(1, numlen):
		if curnum[k]>=curnum[k-1]:
			# this is valid
			dummy=1
		else:
			junctionPoint = k-1
			junctionNum = curnum[junctionPoint]
			# find out if decrementing this junction point will necessitate a propagation. If so, how many
			propagated = 0
			#print junctionPoint,":",junctionNum
			for m in range(1, junctionPoint+1):
				if curnum[junctionPoint-m]>(junctionNum-m):
					propagated += 1
			# 12345267
			curnum[junctionPoint+1-propagated:] = "9"*(numlen-junctionPoint-1+propagated)
			curnum[junctionPoint-propagated] = str(int(curnum[junctionPoint-propagated])-1)
			break
	zerocount = 0
	while len(curnum)>0:
		if curnum[0]=="0":
			curnum = curnum[1:]
		else:
			break
	outstr =  "Case #"+str(i+1)+": "+ "".join(map(str,curnum))
	print outstr
	outhandle.write(outstr+"\n")
outhandle.close()

