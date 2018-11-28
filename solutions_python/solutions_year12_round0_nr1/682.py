str1="y qee"
pstr1="a zoo"
i=-1
a={}
a['z']='q'
a['\n']='\n'

for charac in str1:
    i=i+1
    a[charac]=pstr1[i]
    print pstr1[i]

str1="ejp mysljylc kd kxveddknmc re jsicpdrysi"
pstr1="our language is impossible to understand"

i=-1
for charac in str1:
    i=i+1
    a[charac]=pstr1[i]
    print pstr1[i]


str1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
pstr1="there are twenty six factorial possibilities"

i=-1
for charac in str1:
    i=i+1
    a[charac]=pstr1[i]
    print pstr1[i]

str1="de kr kd eoya kw aej tysr re ujdr lkgc jv"
pstr1="so it is okay if you want to just give up"

i=-1
for charac in str1:
    i=i+1
    a[charac]=pstr1[i]
    print pstr1[i]

strchk="abcdefghijklmnopqrstuvwxyz"
for key in sorted(a.iterkeys()):
    print key + " -> " + a[key]

def convert(strtoconv,a):
    outputstr=""
    for char in strtoconv:
        outputstr=outputstr+a[char]
    return outputstr

file1=open("input.txt",'r')
file2=open("output.txt",'w')

nooflines=int(file1.readline())

for i in range (0,nooflines):
    inpstr=file1.readline()
    opstr=convert(inpstr,a)
    file2.write("Case #"+str(i+1)+": "+opstr)

file2.close();

