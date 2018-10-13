{\rtf1\ansi\ansicpg1252\cocoartf1138\cocoasubrtf320
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 from functools import reduce\
import string, re\
from string import maketrans\
import os\
\
os.chdir("/Users/MichaelLin/Documents/Python_Files/Google_Code_Jam/")\
\
input = re.findall("[a-z]","""\
ejp mysljylc kd kxveddknmc re jsicpdrysi\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
de kr kd eoya kw aej tysr re ujdr lkgc jv qz\
""")\
output = re.findall("[a-z]", """\
our language is impossible to understand\
there are twenty six factorial possibilities\
so it is okay if you want to just give up zq\
""")\
INPUT = open("A-small-attempt2.in.txt", "r")\
input_to_trans = INPUT.read().split("\\n")[1:]\
\
\
def unique(L):\
    rtn = []\
    for e in L:\
        if e not in rtn:\
            rtn.append(e)\
    return rtn\
\
input_un = str(reduce(lambda x,y: x+y, unique(input)))\
output_un = str(reduce(lambda x,y: x+y, unique(output)))\
table = maketrans(input_un, output_un)\
\
\
def make_result(L):\
    result = []\
    for i in range(len(L)-1):\
        result.append("Case #\{0\}: \{1\}".format(i+1, L[i].translate(table)))\
    return result\
\
result = str(reduce(lambda x, y: x +" \\n "+ y, make_result(input_to_trans)))\
\
\
FILE = open("output.txt", "w")\
FILE.writelines(result)\
FILE.close()}