#!/bin/python
dict_code={};
string_googlerese="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
string_language="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
for i in range(0, len(string_googlerese)):
    if string_googlerese[i] not in dict_code.keys():
        dict_code[string_googlerese[i]]=string_language[i]
dict_code['q']='z'
dict_code['z']='q'
input_file=open("A-small-attempt0.in","r")
output_file=open("A-small-attempt0.out","w")
lines=input_file.readlines()
for i in range(0,len(lines)):
    if i==0:
        continue
    if lines[i][-1]=='\n':
        line=lines[i][:-1]
    output_file.write("Case #%d: " % i)
    for ichar in range(0,len(line)):
        output_file.write("%s" % dict_code[line[ichar]])
    output_file.write("\n")
   
