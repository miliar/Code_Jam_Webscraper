#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#XTD:xkocan00

import sys
import codecs
import getopt
import string
import re
import math
import xml.etree.ElementTree as etree
##############################################################################
# napoveda k programu
def usage():
	print ("Napoveda k programu XML2DDL do predmetu IPP - prevod z XML do DDL:\n	Rozhrani programu:\n--help - vypis tehle napovedy\n	--input=soubor -vstupni soubor\n	--output=soubor -nazev souboru, do ktoreho sa ulozi vystup vo formate XML\n	--header=hlavicka -do vystupneho souboru pripoji hlavicku\n	--etc=n urcuje max pocet sloupcu vzniklych ze stejnojmennych podelementu\n	-a -nebudou se generovat sloupce z atributu\n	-b -pokud element bude obsahovat vice stejnojmennych podelementu, bude se uvazovat jako by tu byl pouze jeden takovy\m	-g specialni XML se vztahy\n")

#############################################
#spracovani parametru pomoci knihovny getopt#
#############################################
try:
	opts, args = getopt.getopt(sys.argv[1:], "abg", ["help", "output=", "input=","etc=","header="])
except getopt.GetoptError as err:
	sys.stderr.write("nezname parametre\n")
	usage()
	sys.exit(1)
output ="-"
input ="-"
header ="-"
help = False
countArg=0
icount=0
ocount=0
hcount=0
argc=len(sys.argv)
#Kontroluje se take vicenasobny vyskyt parametru
for arg in sys.argv:
	if arg.rfind("--input")>=0:
		icount=icount+1
		if icount>1:
			sys.stderr.write ("viacnasobna kombinacia parametru --input\n")
			sys.exit(1)
	if arg.rfind("--output")>=0:
		ocount=ocount+1
		if ocount>1:
			sys.stderr.write ("viacnasobna kombinacia parametru --output\n")
			sys.exit(1)
	if arg.rfind("--header")>=0:
		hcount=hcount+1
		if hcount>1:
			sys.stderr.write ("viacnasobna kombinacia parametru --header\n")
			sys.exit(1)
	
	if sys.argv.count(arg)>1:
		sys.stderr.write ("viacnasobna kombinacia parametru %s\n"%arg)
		sys.exit(1)

##Kontrola jednotlivych prepinacu 
##a nastavovani flagu

for o, a in opts:
	if o in ("--help"):
		help = True
	elif o in ("--output"):
		output = a
		countArg=countArg+1
	elif o in ("--input"):
		input = a
		countArg=countArg+1
	else:
		assert False, "Neznamy prepinac"

def ispalindrome(word):
	if len(word) < 2: return True
	if word[0] != word[-1]: return False
	return ispalindrome(word[1:-1])

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

##parametr help se nemuze kombinovat s jinymi prepinaci
if (help):
	if ((a) or (b) or (g) or ((header !="-" )) or ((output !="-")) or ((input !="-"))):
		sys.stderr.write("Parametr --help sa neda kombinovat s inymi par\n")
		sys.exit(1)         
##a take ani parametr etc s parametrem b

if help == True:
	sys.exit(0)
if input=="":
	input="-"
if output=="":
	output="-"
if header=="":
	header="-"
if input !="-" :
	try:
		file = open(input,'r',encoding='utf-8')
	except:
		sys.stderr.write("Zadany subor sa neda otvorit\n")
		sys.exit(1)
           
elif input =="-" : 
	file = sys.stdin.read()
idx=1;
list=[]
for line in file:
	line=line.strip()
	interval=line.split(" ")
	if (len(interval)==2):
		for i in range(int(interval[0]),int(interval[1])+1):
			if (ispalindrome(str(i))):
				if (is_square(i)):
					if (ispalindrome(str(int(math.sqrt(i))))):	
						list.append(i)
		print('Case #'+str(idx)+': '+str(len(list)))
		idx+=1 
		list=[]
