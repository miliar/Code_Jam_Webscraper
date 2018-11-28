#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hema
#
# Created:     14-04-2012
# Copyright:   (c) hema 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string

f = open('A-small-attempt0.in','r')
f2 = open('output.txt','w')
s = f.readline()
j = int(s)
src = string.lowercase[0:26]
for i in range(0,j):
    g = f.readline()
    trans = string.maketrans(src, 'yhesocvxduiglbkrztnwjpfmaq')
    f2.write('Case #'+ str(i+1) + ': '+ string.translate(g, trans))
    f2.flush()
