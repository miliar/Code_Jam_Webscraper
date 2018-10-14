#!/usr/bin/python
import os
import sys
import string

ifile = open(sys.argv[1])
ofile = open("output.out","w")


#create translation dictionary

gdict = {}
gdict['a'] = 'y'
#gdict['o'] = 'e'
gdict['z'] = 'q'
gdict['q'] = 'z'

sample_g_strings = [
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    ]

sample_e_strings = [
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up"
        ]

for i in range(0,len(sample_g_strings)):
    for j in range(0,len(sample_g_strings[i])):
        if sample_g_strings[i][j] in gdict:
            if not gdict[sample_g_strings[i][j]] == sample_e_strings[i][j]:
                print("Crap at: " + sample_g_strings[i][j] + " had: " + gdict[sample_g_strings[i][j]] + " now i have: " + sample_e_strings[i][j])
                exit(1)
        else:
            gdict[sample_g_strings[i][j]] = sample_e_strings[i][j]
            print(sample_g_strings[i][j] + " is " + sample_e_strings[i][j]) 

print gdict

ver_dict = {}
for letter in gdict:
    if gdict[letter] in ver_dict:
        print("double: " + gdict_letter)
    else:
        ver_dict[gdict[letter]] = True

for letter in string.ascii_lowercase:
    if letter not in ver_dict:
        print("missing: " + letter)





i = 0
for line in ifile.readlines()[1:]:
    i += 1
    output_line = "Case #" + str(i) + ": "
    for letter in line.strip():
        output_line += gdict[letter]
    ofile.write(output_line + "\n")
        

                
            
                





    
