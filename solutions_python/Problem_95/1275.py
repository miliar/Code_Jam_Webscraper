#! /usr/bin/env python
#coding=utf-8

filename = r"C:\Users\i035514\Desktop\Codejam\Qualification\A-small-attempt1"

input=file("%s.in" % filename)
output=file("%s.ou" % filename, "w")
T=int(input.readline())

#..........Get Mapping Table.................
googlerese_sample = []
googlerese_sample.append(("y","a"))
googlerese_sample.append(("e","o"))
googlerese_sample.append(("q","z"))
googlerese_sample.append(("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand"))
googlerese_sample.append(("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"))
googlerese_sample.append(("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up"))

mapping = {}
re_mapping={}
mapping[" "] = " "
re_mapping[" "] = " "

for (gr,en) in googlerese_sample:
    for i in xrange(0,len(gr)):
        mapping[gr[i]]=en[i]
        re_mapping[en[i]]=gr[i]
       

if len(mapping)==27:
    print "100% mapping"
elif len(mapping) == 26:
    key=""
    value=""
    for i in xrange(ord('a'),ord('z')+1):
        if not chr(i) in mapping:
            key = chr(i)
    for j in xrange(ord('a'),ord('z')+1):
        if not chr(j) in re_mapping:
            value = chr(j)
    mapping[key]=value
    re_mapping[value]=key
    print "100% mapping"
    
else:
    print "mapping < 100%"


#..........Translate........................

for caseNum in xrange(1,T+1):
    line = input.readline()
    result = ""
    for i in xrange(0,len(line)-1):
        result=result+mapping[line[i]]
 
    
    outstring = "Case #%d: %s\n" % (caseNum, result)
    output.writelines(outstring)

print "Done"
input.close()
output.close()

            
        
        
    
    
    