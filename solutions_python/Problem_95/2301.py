# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 20:57:21 2012

@author: Big one
"""



testin = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
          "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
          "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

testout = ["our language is impossible to understand",
           "there are twenty six factorial possibilities",
           "so it is okay if you want to just give up"]

code = [[0,0]]*26
code[16] = (['q','z'])
code[25] = (['z','q'])

for i in range(len(testin)):
    li = list(testin[i])
    lo = list(testout[i])
    for k in range(len(li)):
        if li[k] == ' ':
            continue
        tup = [li[k],lo[k]]
        if tup not in code:
            print ord(li[k])-97
            code[ord(li[k])-97]= (tup)

a = 0
for eil in code:
    print eil
print len(code)


fi = open('A-small-attempt1.in','r+')
fi.readline()
with open("fileout.txt", "w") as fileout:
    i = 1
    for line in fi:
        #line = line.replace('\n','')
        newline = ""
        for ch in line:
            if ch == '\n' or ch == ' ':
                newline += ch
                continue
            #print ord(ch)-97, ord(ch), ch
            newline += code[ord(ch)-97][1]
     
        fileout.write("Case #%s: " %i)
        fileout.write(newline)
        i += 1


fi.close()